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

    def aggregate_products(self, search_term: str) -> List[Dict]:
        all_raw_data = []
        all_raw_data.extend(self.scrape_priceoye(search_term))
        all_raw_data.extend(self.scrape_daraz(search_term))
        
        from difflib import SequenceMatcher
        def similarity(a, b): return SequenceMatcher(None, a.lower(), b.lower()).ratio()
        
        grouped = []
        used_indices = set()
        for i, p1 in enumerate(all_raw_data):
            if i in used_indices: continue
            cluster = [p1]
            used_indices.add(i)
            for j, p2 in enumerate(all_raw_data):
                if j in used_indices: continue
                if similarity(p1['title'], p2['title']) > 0.6:
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
        return grouped

if __name__ == "__main__":
    scraper = PakistanEcommerceScraper()
    keywords = ['charger', 'iphone 15', 'laptop', 'men shirt', 'car accessories']
    final_data = []
    for word in keywords:
        final_data.extend(scraper.aggregate_products(word))
    
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=4)
