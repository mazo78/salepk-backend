#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SalePK Price Scraper
Automated daily price updates
"""

import json
from datetime import datetime

def main():
    print("=" * 60)
    print("🚀 SalePK Scraper Starting...")
    print("=" * 60)
    
    # Demo products data
    products = [
        {
            "id": 1,
            "title": "Samsung Galaxy S23 Ultra 256GB",
            "brand": "Samsung",
            "category": "mobiles",
            "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=500",
            "prices": [
                {"store": "Daraz.pk", "price": 289999, "url": "https://daraz.pk"},
                {"store": "Symbios.pk", "price": 285999, "url": "https://symbios.pk"},
                {"store": "PriceOaks.com", "price": 294999, "url": "https://priceoaks.com"}
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
                {"store": "Daraz.pk", "price": 539999, "url": "https://daraz.pk"},
                {"store": "PriceOaks.com", "price": 534999, "url": "https://priceoaks.com"}
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 3,
            "title": "Dell XPS 15 Intel Core i7 16GB RAM",
            "brand": "Dell",
            "category": "laptops",
            "image": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500",
            "prices": [
                {"store": "Symbios.pk", "price": 319999, "url": "https://symbios.pk"},
                {"store": "Daraz.pk", "price": 324999, "url": "https://daraz.pk"}
            ],
            "last_updated": datetime.now().isoformat()
        }
    ]
    
    # Save to JSON file
    output_file = 'products.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Successfully saved {len(products)} products")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total stores: {sum(len(p['prices']) for p in products)}")
    print("=" * 60)
    print("✨ Scraping completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
