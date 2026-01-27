import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from typing import List, Dict
import re

class PakistanEcommerceScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def clean_price(self, price_text: str) -> int:
        price_text = re.sub(r'[^\d]', '', price_text)
        try: return int(price_text)
        except: return 0

    def scrape_priceoye(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://priceoye.pk/search?q={search_term.replace(' ', '+')}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Selector update for better results
            items = soup.find_all('div', {'class': 'product-list'})[:5]
            for item in items:
                title = item.find('div', {'class': 'p-title'}).text.strip()
                price = self.clean_price(item.find('div', {'class': 'price-box'}).text)
                link = item.find('a')['href']
                image = item.find('img')['src']
                products.append({'title': title, 'price': price, 'store': 'PriceOye.pk', 'url': link, 'image': image})
        except: pass
        return products

    def scrape_daraz(self, search_term: str) -> List[Dict]:
        products = []
        try:
            url = f"https://www.daraz.pk/catalog/?q={search_term}"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'gridItem--Yd0sa'})[:5]
            for item in items:
                title = item.find('div', {'class': 'title--wFj93'}).text.strip()
                price = self.clean_price(item.find('span', {'class': 'currency--GVKjl'}).text)
                link = "https:" + item.find('a')['href']
                image = item.find('img')['src']
                products.append({'title': title, 'price': price, 'store': 'Daraz.pk', 'url': link, 'image': image})
        except: pass
        return products

    def aggregate_all(self, keywords):
        all_final_data = []
        for word in keywords:
            print(f"🔍 Searching: {word}")
            raw_data = []
            raw_data.extend(self.scrape_priceoye(word))
            raw_data.extend(self.scrape_daraz(word))
            
            # Simple grouping logic
            for item in raw_data:
                all_final_data.append({
                    'title': item['title'],
                    'image': item['image'],
                    'prices': [{'store': item['store'], 'price': item['price'], 'url': item['url']}],
                    'min_price': item['price'],
                    'category': 'general',
                    'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M")
                })
            time.sleep(1) # Block hone se bachne ke liye
        return all_final_data

if __name__ == "__main__":
    scraper = PakistanEcommerceScraper()
    # In keywords ko scraper ab backup mein save karega
    search_list = ['charger', 'baseus charger', 'iphone 15', 'laptop', 'men shirt', 'car accessories']
    
    data = scraper.aggregate_all(search_list)
    
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"✅ Success! Saved {len(data)} products.")
