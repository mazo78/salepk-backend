from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
import requests
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Cache directory for images
CACHE_DIR = "image_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

@app.route('/proxy-image', methods=['GET'])
def proxy_image():
    """Proxy external images to avoid CORS issues"""
    image_url = request.args.get('url')
    
    if not image_url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        # Create a safe filename from URL
        safe_filename = image_url.split('/')[-1].replace('?', '_').replace('&', '_')
        cache_path = os.path.join(CACHE_DIR, safe_filename)
        
        # Check if image is cached
        if os.path.exists(cache_path):
            return send_file(cache_path, mimetype='image/jpeg')
        
        # Fetch image with proper headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://www.google.com/',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
        }
        
        response = requests.get(image_url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()
        
        # Convert to PIL Image and save
        img = Image.open(BytesIO(response.content))
        
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Save to cache
        img.save(cache_path, 'JPEG', quality=85, optimize=True)
        
        return send_file(cache_path, mimetype='image/jpeg')
    
    except requests.exceptions.RequestException as e:
        # Return placeholder image on error
        return jsonify({"error": f"Failed to fetch image: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

@app.route('/placeholder', methods=['GET'])
def placeholder():
    """Return a placeholder image"""
    width = int(request.args.get('w', 300))
    height = int(request.args.get('h', 300))
    
    # Create placeholder image
    img = Image.new('RGB', (width, height), color='#E0E0E0')
    
    buf = BytesIO()
    img.save(buf, 'JPEG')
    buf.seek(0)
    
    return send_file(buf, mimetype='image/jpeg')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "cached_images": len(os.listdir(CACHE_DIR))})

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Image Proxy Server Starting...")
    print("=" * 60)
    print("📡 Server: http://localhost:5000")
    print("🔗 Proxy URL: http://localhost:5000/proxy-image?url=IMAGE_URL")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
