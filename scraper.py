"""
SalePK Price Scraper - GitHub Actions Compatible
Scrapes product prices from Pakistani e-commerce sites
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import re

class PakistanEcommerceScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.products = []

    def clean_price(self, price_text):
        """Extract numeric price from text"""
        if not price_text:
            return 0
        # Remove Rs, PKR, commas, and spaces
        price_text = re.sub(r'[^\d]', '', str(price_text))
        try:
            return int(price_text)
        except:
            return 0

    def scrape_daraz(self, search_term):
        """Scrape Daraz.pk"""
        products = []
        try:
            url = f"https://www.daraz.pk/catalog/?q={search_term.replace(' ', '+')}"
            print(f"Scraping Daraz for: {search_term}")
            
            response = requests.get(url, headers=self.headers, timeout=15)
            if response.status_code != 200:
                print(f"Daraz returned status code: {response.status_code}")
                return products
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Multiple selector strategies for robustness
            selectors = [
                {'item': 'div', 'class': 'gridItem--Yd0sa'},
                {'item': 'div', 'class': 'Bm3ON'},
                {'item': 'div', 'data-qa-locator': 'product-item'}
            ]
            
            items = []
            for selector in selectors:
                items = soup.find_all(selector['item'], class_=selector.get('class'))
                if items:
                    break
            
            print(f"Found {len(items)} items on Daraz")
            
            for idx, item in enumerate(items[:15]):  # Limit to 15 items
                try:
                    # Try multiple title selectors
                    title_elem = (
                        item.find('div', class_='title--wFj93') or
                        item.find('div', class_='RfADt') or
                        item.find('a', {'class': 'title'})
                    )
                    
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    
                    # Try multiple price selectors
                    price_elem = (
                        item.find('span', class_='currency--GVKjl') or
                        item.find('span', class_='aBrP0') or
                        item.find('span', class_='price')
                    )
                    
                    if not price_elem:
                        continue
                    
                    price = self.clean_price(price_elem.get_text())
                    
                    # Get link
                    link_elem = item.find('a')
                    link = "https://www.daraz.pk" + link_elem['href'] if link_elem and link_elem.get('href', '').startswith('/') else link_elem.get('href', 'https://www.daraz.pk')
                    
                    # Get image
                    img_elem = item.find('img')
                    image = img_elem.get('src') or img_elem.get('data-src', '') if img_elem else ''
                    
                    if price > 0 and title:
                        products.append({
                            'title': title,
                            'price': price,
                            'store': 'Daraz.pk',
                            'url': link,
                            'image': image
                        })
                        print(f"  ✓ {title[:50]}... - Rs. {price}")
                        
                except Exception as e:
                    print(f"  × Error parsing Daraz item {idx}: {str(e)[:50]}")
                    continue
                    
        except Exception as e:
            print(f"Error scraping Daraz: {str(e)}")
        
        return products

    def scrape_priceoaks(self, search_term):
        """Scrape PriceOaks - simplified version"""
        products = []
        try:
            url = f"https://priceoaks.com/search?q={search_term.replace(' ', '+')}"
            print(f"Scraping PriceOaks for: {search_term}")
            
            response = requests.get(url, headers=self.headers, timeout=15)
            if response.status_code != 200:
                return products
            
            soup = BeautifulSoup(response.content, 'html.parser')
            # PriceOaks uses different structure - adjust as needed
            print(f"  ⚠ PriceOaks scraping needs site-specific implementation")
            
        except Exception as e:
            print(f"Error scraping PriceOaks: {str(e)}")
        
        return products

    def aggregate_products(self, search_terms):
        """Aggregate products from all sources"""
        all_products = []
        
        for term in search_terms:
            print(f"\n{'='*60}")
            print(f"Searching for: {term}")
            print(f"{'='*60}")
            
            # Scrape Daraz
            daraz_products = self.scrape_daraz(term)
            all_products.extend(daraz_products)
            
            print(f"Found {len(daraz_products)} products for '{term}'")
            
            # Add delay to avoid rate limiting
            time.sleep(3)
        
        # Group similar products
        grouped = self.group_similar_products(all_products)
        
        return grouped

    def group_similar_products(self, products):
        """Group products with similar titles"""
        from difflib import SequenceMatcher
        
        def similarity(a, b):
            return SequenceMatcher(None, a.lower(), b.lower()).ratio()
        
        grouped_products = []
        used_indices = set()
        
        for i, product in enumerate(products):
            if i in used_indices:
                continue
                
            similar_products = [product]
            used_indices.add(i)
            
            for j, other_product in enumerate(products):
                if j in used_indices or j <= i:
                    continue
                    
                if similarity(product['title'], other_product['title']) > 0.7:
                    similar_products.append(other_product)
                    used_indices.add(j)
            
            # Create aggregated product
            base_product = similar_products[0]
            
            # Extract brand
            brand = self.extract_brand(base_product['title'])
            category = self.categorize_product(base_product['title'])
            
            grouped_products.append({
                'id': len(grouped_products) + 1,
                'title': base_product['title'],
                'image': base_product['image'] or 'https://via.placeholder.com/300',
                'category': category,
                'brand': brand,
                'prices': [
                    {
                        'store': p['store'],
                        'price': p['price'],
                        'url': p['url']
                    } for p in similar_products
                ],
                'last_updated': datetime.now().isoformat()
            })
        
        return grouped_products

    def extract_brand(self, title):
        """Extract brand from title"""
        brands = [
            'Samsung', 'Apple', 'iPhone', 'Dell', 'HP', 'Lenovo', 'Sony', 
            'LG', 'Xiaomi', 'Oppo', 'Vivo', 'Realme', 'Huawei', 'OnePlus',
            'Asus', 'Acer', 'MSI', 'Razer', 'Canon', 'Nikon', 'Nike', 'Adidas'
        ]
        
        title_lower = title.lower()
        for brand in brands:
            if brand.lower() in title_lower:
                return brand
        
        # Return first word if no brand found
        return title.split()[0] if title else 'Unknown'

    def categorize_product(self, title):
        """Categorize product based on title"""
        title_lower = title.lower()
        
        if any(word in title_lower for word in ['phone', 'mobile', 'smartphone', 'iphone', 'samsung galaxy']):
            return 'mobiles'
        elif any(word in title_lower for word in ['laptop', 'notebook', 'macbook', 'chromebook']):
            return 'laptops'
        elif any(word in title_lower for word in ['tv', 'television', 'led', 'smart tv']):
            return 'electronics'
        elif any(word in title_lower for word in ['headphone', 'earphone', 'airpods', 'buds']):
            return 'electronics'
        elif any(word in title_lower for word in ['watch', 'smartwatch']):
            return 'electronics'
        elif any(word in title_lower for word in ['shoe', 'sneaker', 'boot']):
            return 'fashion'
        elif any(word in title_lower for word in ['shirt', 't-shirt', 'jeans', 'dress']):
            return 'fashion'
        else:
            return 'general'

    def save_to_json(self, products, filename='products.json'):
        """Save products to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=2)
        print(f"\n✓ Saved {len(products)} products to {filename}")


def main():
    """Main execution"""
    print("="*60)
    print("🚀 SalePK Price Scraper - Starting...")
    print("="*60)
    
    scraper = PakistanEcommerceScraper()
    
    # Popular search terms
    search_terms = [
        'samsung mobile',
        'iphone',
        'laptop dell',
        'macbook',
        'smart tv',
        'wireless headphones'
    ]
    
    print(f"\nSearching for {len(search_terms)} categories...")
    
    try:
        all_products = scraper.aggregate_products(search_terms)
        
        print(f"\n{'='*60}")
        print(f"📊 Scraping Summary")
        print(f"{'='*60}")
        print(f"Total unique products: {len(all_products)}")
        print(f"Categories found: {len(set(p['category'] for p in all_products))}")
        
        # Save results
        scraper.save_to_json(all_products, 'products.json')
        
        print(f"\n✅ Scraping completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during scraping: {str(e)}")
        # Create empty file to prevent errors
        scraper.save_to_json([], 'products.json')
        raise


if __name__ == "__main__":
    main()
