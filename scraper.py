"""
SalePK Web Scraper
Auto-updates product prices daily
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

print("🚀 Starting SalePK Scraper...")

# Sample products (replace with real scraping later)
products = [
    {
        "id": 1,
        "title": "Samsung Galaxy S23 Ultra 256GB",
        "brand": "Samsung",
        "category": "mobiles",
        "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=500",
        "prices": [
            {"store": "Daraz.pk", "price": 289999, "url": "https://daraz.pk"},
            {"store": "Symbios.pk", "price": 285999, "url": "https://symbios.pk"}
        ],
        "last_updated": datetime.now().isoformat()
    },
    {
        "id": 2,
        "title": "iPhone 15 Pro Max 512GB",
        "brand": "Apple",
        "category": "mobiles",
        "image": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500",
        "prices": [
            {"store": "Telemart.pk", "price": 529999, "url": "https://telemart.pk"},
            {"store": "Daraz.pk", "price": 539999, "url": "https://daraz.pk"}
        ],
        "last_updated": datetime.now().isoformat()
    }
]

# Save to JSON
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully saved {len(products)} products!")
print("📁 File: products.json created")
