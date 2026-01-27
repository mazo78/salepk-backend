import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from typing import List, Dict
import re

class PakistanEcommerceScraper:
    def __init__(self):
        # Latest 2026 User-Agent taake block na ho
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def clean_price(self, price_text: str) -> int:
        price_text = re.sub(r'[^\d]', '', price_text)
        try:
            return int(price_text)
        except:
            return 0

    # 1. PRICE OYE (Best for Mobiles/Tech)
    def scrape_priceoye(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://priceoye.pk/search?q={search_term.replace(' ', '+')}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'product-list'})[:10]
            for item in items:
                title = item.find('div', {'class': 'p-title'}).text.strip()
                price = self.clean_price(item.find('div', {'class': 'price-box'}).text)
                link = item.find('a')['href']
                image = item.find('img')['src']
                products.append({'title': title, 'price': price, 'store': 'PriceOye.pk', 'url': link, 'image': image})
        except Exception as e: print(f"PriceOye Error: {e}")
        return products

    # 2. SHOPHIVE (Best for Laptops/Apple)
    def scrape_shophive(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://www.shophive.com/catalogsearch/result/?q={search_term}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'product-item-info'})[:10]
            for item in items:
                title = item.find('a', {'class': 'product-item-link'}).text.strip()
                price = self.clean_price(item.find('span', {'data-price-type': 'finalPrice'}).text)
                link = item.find('a', {'class': 'product-item-link'})['href']
                image = item.find('img', {'class': 'product-image-photo'})['src']
                products.append({'title': title, 'price': price, 'store': 'Shophive.com', 'url': link, 'image': image})
        except Exception as e: print(f"Shophive Error: {e}")
        return products

    # 3. TELEMART (General Electronics)
    def scrape_telemart(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://www.telemart.pk/search?q={search_term}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'product-item-container'})[:10]
            for item in items:
                title = item.find('h4').text.strip()
                price = self.clean_price(item.find('span', {'class': 'price'}).text)
                link = "https://www.telemart.pk" + item.find('a')['href']
                image = item.find('img')['src']
                products.append({'title': title, 'price': price, 'store': 'Telemart.pk', 'url': link, 'image': image})
        except Exception as e: print(f"Telemart Error: {e}")
        return products

    # 4. VMART (Best for Gaming/PC Parts)
    def scrape_vmart(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://www.vmart.pk/search?q={search_term}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'product-inner'})[:10]
            for item in items:
                title = item.find('a', {'class': 'product-title'}).text.strip()
                price = self.clean_price(item.find('span', {'class': 'price'}).text)
                link = item.find('a')['href']
                image = item.find('img')['src']
                products.append({'title': title, 'price': price, 'store': 'Vmart.pk', 'url': link, 'image': image})
        except Exception as e: print(f"Vmart Error: {e}")
        return products

    # 5. DARAZ (Marketplace)
    def scrape_daraz(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://www.daraz.pk/catalog/?q={search_term}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'gridItem--Yd0sa'})[:10]
            for item in items:
                title = item.find('div', {'class': 'title--wFj93'}).text.strip()
                price = self.clean_price(item.find('span', {'class': 'currency--GVKjl'}).text)
                link = "https:" + item.find('a')['href']
                image = item.find('img')['src']
                products.append({'title': title, 'price': price, 'store': 'Daraz.pk', 'url': link, 'image': image})
        except Exception as e: print(f"Daraz Error: {e}")
        return products

    def aggregate_products(self, search_term: str) -> List[Dict]:
        print(f"🔍 Searching for: {search_term}")
        all_raw_data = []
        all_raw_data.extend(self.scrape_priceoye(search_term))
        time.sleep(1)
        all_raw_data.extend(self.scrape_shophive(search_term))
        time.sleep(1)
        all_raw_data.extend(self.scrape_telemart(search_term))
        all_raw_data.extend(self.scrape_vmart(search_term))
        all_raw_data.extend(self.scrape_daraz(search_term))
        return self.group_similar_products(all_raw_data)

    def group_similar_products(self, products: List[Dict]) -> List[Dict]:
        from difflib import SequenceMatcher
        def similarity(a, b): return SequenceMatcher(None, a.lower(), b.lower()).ratio()
        
        grouped = []
        used_indices = set()
        for i, p1 in enumerate(products):
            if i in used_indices: continue
            cluster = [p1]
            used_indices.add(i)
            for j, p2 in enumerate(products):
                if j in used_indices: continue
                if similarity(p1['title'], p2['title']) > 0.65:
                    cluster.append(p2)
                    used_indices.add(j)
            
            best = cluster[0]
            grouped.append({
                'title': best['title'],
                'image': best['image'],
                'prices': [{'store': p['store'], 'price': p['price'], 'url': p['url']} for p in cluster],
                'min_price': min(p['price'] for p in cluster),
                'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
        return sorted(grouped, key=lambda x: x['min_price'])

    def save_to_json(self, data):
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Data saved to products.json. Total groups: {len(data)}")

# --- RUN WITH ALL CATEGORIES ---
if __name__ == "__main__":
    scraper = PakistanEcommerceScraper()
    
    # Yahan humne saari categories ke top keywords add kar diye hain
    keywords = [
        # Electronics
        'charger', 'baseus fast charger', 'power bank 20000mah', 'wireless earbuds', 'bluetooth speaker',
        # Mobiles
        'iphone 15 pro max', 'samsung s24 ultra', 'redmi note 13', 'infinix hot 40',
        # Computers
        'gaming laptop', 'macbook air m2', 'hp victus', 'wireless mouse', 'gaming monitor',
        # Garion ka saman (Car Accessories)
        'car dash cam', 'car air purifier', 'tyre inflator portable', 'car vacuum cleaner',
        # Clothes & Fashion
        'men shirt cotton', 'women lawn suit', 'winter jacket', 'leather wallet', 'smart watch'
    ]
    
    final_data = []
    for word in keywords:
        results = scraper.aggregate_products(word)
        final_data.extend(results)
    
    scraper.save_to_json(final_data)
