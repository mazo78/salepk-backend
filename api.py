"""
SalePK API Backend - Flask Server
Serves product data to the frontend

Requirements:
pip install flask flask-cors pymongo
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Load products from JSON file
def load_products():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Or use MongoDB
def load_products_from_mongodb():
    try:
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017/')
        db = client['salepk']
        products = list(db['products'].find({}, {'_id': 0}))
        return products
    except:
        return []


@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products with optional filtering"""
    products = load_products()
    
    # Get query parameters
    category = request.args.get('category')
    search = request.args.get('search')
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    sort_by = request.args.get('sort', 'price-low')
    
    # Apply filters
    filtered_products = products
    
    if category and category != 'all':
        filtered_products = [p for p in filtered_products if p.get('category') == category]
    
    if search:
        search = search.lower()
        filtered_products = [
            p for p in filtered_products 
            if search in p.get('title', '').lower() or search in p.get('brand', '').lower()
        ]
    
    if min_price is not None or max_price is not None:
        def get_min_price(product):
            prices = product.get('prices', [])
            return min([p['price'] for p in prices]) if prices else 0
        
        if min_price is not None:
            filtered_products = [p for p in filtered_products if get_min_price(p) >= min_price]
        
        if max_price is not None:
            filtered_products = [p for p in filtered_products if get_min_price(p) <= max_price]
    
    # Sort products
    def get_min_price(product):
        prices = product.get('prices', [])
        return min([p['price'] for p in prices]) if prices else 0
    
    if sort_by == 'price-low':
        filtered_products.sort(key=get_min_price)
    elif sort_by == 'price-high':
        filtered_products.sort(key=get_min_price, reverse=True)
    
    return jsonify({
        'success': True,
        'count': len(filtered_products),
        'products': filtered_products
    })


@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product by ID"""
    products = load_products()
    product = next((p for p in products if p.get('id') == product_id), None)
    
    if product:
        return jsonify({
            'success': True,
            'product': product
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Product not found'
        }), 404


@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all available categories"""
    products = load_products()
    categories = list(set([p.get('category', 'general') for p in products]))
    
    return jsonify({
        'success': True,
        'categories': categories
    })


@app.route('/api/stores', methods=['GET'])
def get_stores():
    """Get all stores we scrape from"""
    stores = [
        {'name': 'Daraz.pk', 'url': 'https://daraz.pk'},
        {'name': 'PriceOaks.com', 'url': 'https://priceoaks.com'},
        {'name': 'iShopping.pk', 'url': 'https://ishopping.pk'},
        {'name': 'Symbios.pk', 'url': 'https://symbios.pk'},
        {'name': 'Telemart.pk', 'url': 'https://telemart.pk'}
    ]
    
    return jsonify({
        'success': True,
        'stores': stores
    })


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get platform statistics"""
    products = load_products()
    
    # Calculate stats
    total_products = len(products)
    total_stores = 5
    
    # Calculate average savings
    total_savings = 0
    savings_count = 0
    
    for product in products:
        prices = product.get('prices', [])
        if len(prices) > 1:
            min_price = min([p['price'] for p in prices])
            max_price = max([p['price'] for p in prices])
            savings_percent = ((max_price - min_price) / max_price) * 100
            total_savings += savings_percent
            savings_count += 1
    
    avg_savings = int(total_savings / savings_count) if savings_count > 0 else 0
    
    return jsonify({
        'success': True,
        'stats': {
            'total_products': total_products,
            'total_stores': total_stores,
            'avg_savings': avg_savings,
            'daily_updates': 50000
        }
    })


@app.route('/api/search', methods=['POST'])
def search_products():
    """Search products"""
    data = request.get_json()
    search_term = data.get('search', '').lower()
    
    products = load_products()
    
    if not search_term:
        return jsonify({
            'success': True,
            'count': len(products),
            'products': products
        })
    
    # Search in title and brand
    results = [
        p for p in products 
        if search_term in p.get('title', '').lower() or 
           search_term in p.get('brand', '').lower()
    ]
    
    return jsonify({
        'success': True,
        'count': len(results),
        'products': results
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    print("Starting SalePK API Server...")
    print("API running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
