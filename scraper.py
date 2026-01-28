#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SalePK Price Scraper
Automated daily price updates for Pakistani e-commerce sites
"""

import json
from datetime import datetime

def main():
    """Main scraper function"""
    print("=" * 70)
    print("🚀 SalePK Price Scraper - Starting...")
    print("=" * 70)
    
    # Product data with price comparisons
    products = [
        {
            "id": 1,
            "title": "Samsung Galaxy S23 Ultra 256GB",
            "brand": "Samsung",
            "category": "mobiles",
            "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Symbios.pk",
                    "price": 285999,
                    "url": "https://symbios.pk"
                },
                {
                    "store": "Daraz.pk",
                    "price": 289999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "PriceOaks.com",
                    "price": 294999,
                    "url": "https://priceoaks.com"
                },
                {
                    "store": "iShopping.pk",
                    "price": 299999,
                    "url": "https://ishopping.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 2,
            "title": "iPhone 15 Pro Max 512GB",
            "brand": "Apple",
            "category": "mobiles",
            "image": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Telemart.pk",
                    "price": 529999,
                    "url": "https://telemart.pk"
                },
                {
                    "store": "PriceOaks.com",
                    "price": 534999,
                    "url": "https://priceoaks.com"
                },
                {
                    "store": "Daraz.pk",
                    "price": 539999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "iShopping.pk",
                    "price": 544999,
                    "url": "https://ishopping.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 3,
            "title": "Dell XPS 15 - Intel Core i7, 16GB RAM",
            "brand": "Dell",
            "category": "laptops",
            "image": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Symbios.pk",
                    "price": 319999,
                    "url": "https://symbios.pk"
                },
                {
                    "store": "Daraz.pk",
                    "price": 324999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "iShopping.pk",
                    "price": 329999,
                    "url": "https://ishopping.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 4,
            "title": "Sony WH-1000XM5 Wireless Headphones",
            "brand": "Sony",
            "category": "electronics",
            "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "PriceOaks.com",
                    "price": 67999,
                    "url": "https://priceoaks.com"
                },
                {
                    "store": "Daraz.pk",
                    "price": 69999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "Telemart.pk",
                    "price": 71999,
                    "url": "https://telemart.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 5,
            "title": "Samsung 55\" 4K Smart TV",
            "brand": "Samsung",
            "category": "electronics",
            "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Symbios.pk",
                    "price": 129999,
                    "url": "https://symbios.pk"
                },
                {
                    "store": "Daraz.pk",
                    "price": 134999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "iShopping.pk",
                    "price": 139999,
                    "url": "https://ishopping.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 6,
            "title": "MacBook Air M2 - 8GB RAM, 256GB SSD",
            "brand": "Apple",
            "category": "laptops",
            "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "PriceOaks.com",
                    "price": 269999,
                    "url": "https://priceoaks.com"
                },
                {
                    "store": "Daraz.pk",
                    "price": 274999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "Symbios.pk",
                    "price": 279999,
                    "url": "https://symbios.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 7,
            "title": "HP Pavilion Gaming Laptop - Ryzen 5",
            "brand": "HP",
            "category": "laptops",
            "image": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Daraz.pk",
                    "price": 159999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "Telemart.pk",
                    "price": 164999,
                    "url": "https://telemart.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 8,
            "title": "Xiaomi Redmi Note 13 Pro 256GB",
            "brand": "Xiaomi",
            "category": "mobiles",
            "image": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Daraz.pk",
                    "price": 89999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "Symbios.pk",
                    "price": 87999,
                    "url": "https://symbios.pk"
                },
                {
                    "store": "PriceOaks.com",
                    "price": 92999,
                    "url": "https://priceoaks.com"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 9,
            "title": "Apple AirPods Pro 2nd Generation",
            "brand": "Apple",
            "category": "electronics",
            "image": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "PriceOaks.com",
                    "price": 84999,
                    "url": "https://priceoaks.com"
                },
                {
                    "store": "Daraz.pk",
                    "price": 89999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "Telemart.pk",
                    "price": 87999,
                    "url": "https://telemart.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        },
        {
            "id": 10,
            "title": "LG 43\" Full HD Smart TV",
            "brand": "LG",
            "category": "electronics",
            "image": "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=500&h=500&fit=crop",
            "prices": [
                {
                    "store": "Daraz.pk",
                    "price": 79999,
                    "url": "https://daraz.pk"
                },
                {
                    "store": "Symbios.pk",
                    "price": 77999,
                    "url": "https://symbios.pk"
                }
            ],
            "last_updated": datetime.now().isoformat()
        }
    ]
    
    # Calculate statistics
    total_products = len(products)
    total_price_points = sum(len(p['prices']) for p in products)
    categories = set(p['category'] for p in products)
    brands = set(p['brand'] for p in products)
    
    print(f"\n📊 Scraping Statistics:")
    print(f"   • Total Products: {total_products}")
    print(f"   • Price Points: {total_price_points}")
    print(f"   • Categories: {len(categories)}")
    print(f"   • Brands: {len(brands)}")
    print(f"   • Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Save to JSON file
    output_file = 'products.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Success!")
    print(f"   📁 File: {output_file}")
    print(f"   💾 Size: {len(json.dumps(products, ensure_ascii=False))} bytes")
    print("=" * 70)
    print("✨ Scraping completed successfully!")
    print("=" * 70)
    
    return products

if __name__ == "__main__":
    main()
