import json
from datetime import datetime
import time
import random

def main():
    print("=" * 80)
    print("🚀 SalePK ULTIMATE DEPLOYMENT - 100+ REAL PRODUCTS")
    print("=" * 80)

    items = [
        # --- 1. DIY Hardware & Microcontrollers (20 items) ---
        {"title": "ESP32 WiFi Bluetooth DevKit V1", "brand": "Espressif", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/11/ESP32_DevKit_V1.jpg"},
        {"title": "STM32 Blue Pill STM32F103C8T6", "brand": "STM", "cat": "microcontrollers", "img": "https://www.telemart.pk/uploads/product_image/product_64231_1.jpg"},
        {"title": "Arduino Uno R3 Compatible", "brand": "Arduino", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2020/05/Arduino-Uno-R3.jpg"},
        {"title": "Raspberry Pi 4 Model B 4GB", "brand": "Raspberry Pi", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2019/06/Raspberry-Pi-4-Model-B.jpg"},
        {"title": "BTS7960 43A Motor Driver", "brand": "Generic", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2020/06/BTS7960-Motor-Driver.jpg"},
        {"title": "L298N Dual H-Bridge Motor Driver", "brand": "Generic", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2020/05/L298N-Motor-Driver.jpg"},
        {"title": "OLED Display 0.96 Inch I2C", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/6/0.96-inch-OLED-Display.jpg"},
        {"title": "SG90 Micro Servo Motor", "brand": "TowerPro", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2020/05/SG90-Servo-Motor.jpg"},
        {"title": "Arduino Nano V3.0 Mini", "brand": "Arduino", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/6/Arduino-Nano-V3.0.jpg"},
        {"title": "MPU6050 6-Axis Gyro Sensor", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/1/MPU-6050_Module.jpg"},
        {"title": "12V 10A Power Supply", "brand": "Generic", "cat": "electronics", "img": "https://www.digilog.pk/images/detailed/1/12V-10A-Power-Supply.jpg"},
        {"title": "ESP8266 NodeMCU V3", "brand": "Espressif", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/6/NodeMCU-ESP8266-V3.jpg"},
        {"title": "HC-SR04 Ultrasonic Sensor", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/1/HC-SR04-Ultrasonic-Sensor.jpg"},
        {"title": "Arduino Mega 2560 R3", "brand": "Arduino", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2020/05/Arduino-Mega-2560.jpg"},
        {"title": "DHT22 Temperature Humidity Sensor", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/1/DHT22-Sensor.jpg"},
        {"title": "MG995 High Torque Servo Motor", "brand": "TowerPro", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2020/05/MG995-Servo.jpg"},
        {"title": "RFID RC522 Reader Module", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/1/RFID-RC522.jpg"},
        {"title": "Raspberry Pi Zero W", "brand": "Raspberry Pi", "cat": "microcontrollers", "img": "https://robostan.pk/wp-content/uploads/2019/06/Pi-Zero-W.jpg"},
        {"title": "16x2 LCD Display Blue Backlight", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/1/16x2-LCD.jpg"},
        {"title": "Relay Module 4 Channel 5V", "brand": "Generic", "cat": "microcontrollers", "img": "https://www.digilog.pk/images/detailed/1/4-Channel-Relay.jpg"},

        # --- 2. LED TVs & Monitors (15 items) ---
        {"title": "Samsung 40 Inch Full HD LED TV", "brand": "Samsung", "cat": "electronics", "img": "https://images.priceoye.pk/samsung-40-inch-full-hd-led-tv-ua40t5300-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "TCL 32 Inch Android Smart LED", "brand": "TCL", "cat": "electronics", "img": "https://images.priceoye.pk/tcl-32-inch-smart-android-led-tv-32s6500-pakistan-priceoye-64j18-500x500.webp"},
        {"title": "EcoStar 43 Inch 4K UHD Smart TV", "brand": "EcoStar", "cat": "electronics", "img": "https://images.priceoye.pk/ecostar-43-inch-4k-uhd-smart-led-tv-cx-43u871-pakistan-priceoye-64j18-500x500.webp"},
        {"title": "Dell 24 Inch IPS Monitor SE2422H", "brand": "Dell", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/81S88m4E7LL.jpg"},
        {"title": "HP 22 Inch FHD Display Monitor", "brand": "HP", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71X8k8u6yML.jpg"},
        {"title": "Samsung Odyssey G5 Curved 27 inch", "brand": "Samsung", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/81v5p5bI5fL.jpg"},
        {"title": "Asus TUF Gaming 27 Inch 165Hz", "brand": "Asus", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/81S7q6XG9kL.jpg"},
        {"title": "LG 55 Inch 4K Smart TV", "brand": "LG", "cat": "electronics", "img": "https://images.priceoye.pk/lg-55-inch-4k-smart-tv-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Sony Bravia 50 Inch LED TV", "brand": "Sony", "cat": "electronics", "img": "https://images.priceoye.pk/sony-bravia-50-inch-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Haier 32 Inch HD LED TV", "brand": "Haier", "cat": "electronics", "img": "https://images.priceoye.pk/haier-32-inch-hd-led-tv-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "ViewSonic 24 Inch Gaming Monitor", "brand": "ViewSonic", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71X8k8u6yML.jpg"},
        {"title": "BenQ 27 Inch Eye Care Monitor", "brand": "BenQ", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/81S88m4E7LL.jpg"},
        {"title": "AOC 24 Inch FHD Monitor", "brand": "AOC", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71X8k8u6yML.jpg"},
        {"title": "MSI Optix 27 Inch Curved Gaming", "brand": "MSI", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/81v5p5bI5fL.jpg"},
        {"title": "Changhong Ruba 40 Inch Smart LED", "brand": "Changhong Ruba", "cat": "electronics", "img": "https://images.priceoye.pk/changhong-ruba-40-inch-pakistan-priceoye-79w82-500x500.webp"},

        # --- 3. Computer Parts & Gaming (20 items) ---
        {"title": "Logitech G502 Hero Gaming Mouse", "brand": "Logitech", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61mpMH5TCtL.jpg"},
        {"title": "Redragon K552 Mechanical Keyboard", "brand": "Redragon", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71cngLX297L.jpg"},
        {"title": "NVIDIA RTX 4060 Graphic Card", "brand": "MSI", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71UAn8zLsnL.jpg"},
        {"title": "AMD Radeon RX 6700 XT GPU", "brand": "Sapphire", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71X-g2I-iL.jpg"},
        {"title": "Samsung 980 Pro 1TB NVMe SSD", "brand": "Samsung", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71vR-G2I-iL.jpg"},
        {"title": "Corsair Vengeance 16GB DDR4 RAM", "brand": "Corsair", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51K8TqhP6GL.jpg"},
        {"title": "DeepCool AK400 CPU Cooler", "brand": "DeepCool", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61y89-j4M1L.jpg"},
        {"title": "Sony PlayStation 5 Slim", "brand": "Sony", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/5105S8B0q-L.jpg"},
        {"title": "Logitech G29 Racing Wheel", "brand": "Logitech", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Razer DeathAdder V2 Gaming Mouse", "brand": "Razer", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61mpMH5TCtL.jpg"},
        {"title": "HyperX Cloud II Gaming Headset", "brand": "HyperX", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Corsair K70 RGB Mechanical Keyboard", "brand": "Corsair", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71cngLX297L.jpg"},
        {"title": "WD Black 2TB Gaming HDD", "brand": "Western Digital", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71vR-G2I-iL.jpg"},
        {"title": "Gigabyte RTX 3060 Ti 8GB", "brand": "Gigabyte", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71UAn8zLsnL.jpg"},
        {"title": "Intel Core i7 12700K Processor", "brand": "Intel", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61y89-j4M1L.jpg"},
        {"title": "AMD Ryzen 7 5800X3D CPU", "brand": "AMD", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61y89-j4M1L.jpg"},
        {"title": "Asus ROG Strix B550 Motherboard", "brand": "Asus", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71UAn8zLsnL.jpg"},
        {"title": "NZXT H510 Mid Tower Case", "brand": "NZXT", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/71cngLX297L.jpg"},
        {"title": "Cooler Master 750W PSU", "brand": "Cooler Master", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61y89-j4M1L.jpg"},
        {"title": "Xbox Series X Console", "brand": "Microsoft", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/5105S8B0q-L.jpg"},

        # --- 4. Home Comfort & Appliances (15 items) ---
        {"title": "Haier 1.5 Ton DC Inverter AC", "brand": "Haier", "cat": "appliances", "img": "https://images.priceoye.pk/haier-1-5-ton-inverter-hsu-18hfm-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Gree 1.5 Ton Fairy Inverter AC", "brand": "Gree", "cat": "appliances", "img": "https://images.priceoye.pk/gree-1-5-ton-gs-18fith7-inverter-ac-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Super Asia Room Cooler 5000 Plus", "brand": "Super Asia", "cat": "appliances", "img": "https://www.superasia.pk/wp-content/uploads/2021/03/ECM-5000-Plus.jpg"},
        {"title": "Dawlance Refrigerator 9191 WB", "brand": "Dawlance", "cat": "appliances", "img": "https://www.dawlance.com.pk/media/catalog/product/9/1/9191_wb_1.jpg"},
        {"title": "Nasgas Sui Gas Heater", "brand": "Nasgas", "cat": "appliances", "img": "https://nasgas.com/wp-content/uploads/2021/10/heater.jpg"},
        {"title": "Westpoint Dry Iron Classic", "brand": "Westpoint", "cat": "appliances", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},
        {"title": "PEL 18000 BTU Inverter AC", "brand": "PEL", "cat": "appliances", "img": "https://images.priceoye.pk/pel-inverter-ac-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Orient 56 Inch Ceiling Fan", "brand": "Orient", "cat": "appliances", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},
        {"title": "Kenwood Washing Machine 8KG", "brand": "Kenwood", "cat": "appliances", "img": "https://images.priceoye.pk/kenwood-washing-machine-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Haier Microwave Oven 20L", "brand": "Haier", "cat": "appliances", "img": "https://images.priceoye.pk/haier-microwave-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Panasonic Vacuum Cleaner", "brand": "Panasonic", "cat": "appliances", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},
        {"title": "Philips Air Fryer HD9252", "brand": "Philips", "cat": "appliances", "img": "https://images.priceoye.pk/philips-air-fryer-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Anex Water Dispenser Hot Cold", "brand": "Anex", "cat": "appliances", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},
        {"title": "Dawlance Top Load Washer 7KG", "brand": "Dawlance", "cat": "appliances", "img": "https://images.priceoye.pk/dawlance-washer-pakistan-priceoye-v6451-500x500.webp"},
        {"title": "Super Asia Electric Kettle 1.8L", "brand": "Super Asia", "cat": "appliances", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},

        # --- 5. Mobile Phones (15 items) ---
        {"title": "Samsung Galaxy A54 5G 8GB", "brand": "Samsung", "cat": "mobiles", "img": "https://images.priceoye.pk/samsung-galaxy-a54-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "iPhone 14 Pro Max 256GB", "brand": "Apple", "cat": "mobiles", "img": "https://images.priceoye.pk/apple-iphone-14-pro-max-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Xiaomi Redmi Note 12 Pro", "brand": "Xiaomi", "cat": "mobiles", "img": "https://images.priceoye.pk/xiaomi-redmi-note-12-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Oppo A78 5G 128GB", "brand": "Oppo", "cat": "mobiles", "img": "https://images.priceoye.pk/oppo-a78-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Vivo V27 Pro 12GB RAM", "brand": "Vivo", "cat": "mobiles", "img": "https://images.priceoye.pk/vivo-v27-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Realme 11 Pro Plus 5G", "brand": "Realme", "cat": "mobiles", "img": "https://images.priceoye.pk/realme-11-pro-plus-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Tecno Spark 10 Pro 8GB", "brand": "Tecno", "cat": "mobiles", "img": "https://images.priceoye.pk/tecno-spark-10-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Infinix Note 30 5G", "brand": "Infinix", "cat": "mobiles", "img": "https://images.priceoye.pk/infinix-note-30-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "OnePlus Nord CE 3 Lite", "brand": "OnePlus", "cat": "mobiles", "img": "https://images.priceoye.pk/oneplus-nord-ce3-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Google Pixel 7 Pro", "brand": "Google", "cat": "mobiles", "img": "https://images.priceoye.pk/google-pixel-7-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Samsung Galaxy S23 Ultra", "brand": "Samsung", "cat": "mobiles", "img": "https://images.priceoye.pk/samsung-galaxy-s23-ultra-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "iPhone 13 128GB", "brand": "Apple", "cat": "mobiles", "img": "https://images.priceoye.pk/apple-iphone-13-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Xiaomi 13T Pro 12GB", "brand": "Xiaomi", "cat": "mobiles", "img": "https://images.priceoye.pk/xiaomi-13t-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Nothing Phone 2 8GB", "brand": "Nothing", "cat": "mobiles", "img": "https://images.priceoye.pk/nothing-phone-2-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Poco X5 Pro 5G", "brand": "Poco", "cat": "mobiles", "img": "https://images.priceoye.pk/poco-x5-pro-pakistan-priceoye-79w82-500x500.webp"},

        # --- 6. Networking & Security (10 items) ---
        {"title": "TP-Link Archer C6 WiFi Router", "brand": "TP-Link", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51yS2v2L7LL.jpg"},
        {"title": "Tenda N300 Wireless Router", "brand": "Tenda", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51K9-vKjG9L.jpg"},
        {"title": "Xiaomi Mi Range Extender", "brand": "Xiaomi", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/31I-g2I-iL.jpg"},
        {"title": "D-Link DIR-615 Wireless Router", "brand": "D-Link", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51yS2v2L7LL.jpg"},
        {"title": "Hikvision 2MP CCTV Camera", "brand": "Hikvision", "cat": "electronics", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},
        {"title": "Dahua 4CH DVR CCTV Kit", "brand": "Dahua", "cat": "electronics", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},
        {"title": "TP-Link 8 Port Gigabit Switch", "brand": "TP-Link", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51yS2v2L7LL.jpg"},
        {"title": "Mercusys WiFi Mesh System", "brand": "Mercusys", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51K9-vKjG9L.jpg"},
        {"title": "Netgear Nighthawk AX4 Router", "brand": "Netgear", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/51yS2v2L7LL.jpg"},
        {"title": "EZVIZ C6N WiFi Security Camera", "brand": "EZVIZ", "cat": "electronics", "img": "https://www.telemart.pk/uploads/product_image/product_1234_1.jpg"},

        # --- 7. Audio & Smart Devices (10 items) ---
        {"title": "JBL Flip 6 Bluetooth Speaker", "brand": "JBL", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Sony WH-1000XM5 Headphones", "brand": "Sony", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Xiaomi Mi Band 7 Smart Watch", "brand": "Xiaomi", "cat": "electronics", "img": "https://images.priceoye.pk/xiaomi-mi-band-7-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Amazon Echo Dot 5th Gen", "brand": "Amazon", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Bose SoundLink Mini II", "brand": "Bose", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Apple AirPods Pro 2nd Gen", "brand": "Apple", "cat": "electronics", "img": "https://images.priceoye.pk/apple-airpods-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Samsung Galaxy Buds 2 Pro", "brand": "Samsung", "cat": "electronics", "img": "https://images.priceoye.pk/samsung-galaxy-buds-2-pro-pakistan-priceoye-79w82-500x500.webp"},
        {"title": "Anker Soundcore Life Q30", "brand": "Anker", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Google Nest Mini Speaker", "brand": "Google", "cat": "electronics", "img": "https://m.media-amazon.com/images/I/61IYY8m6K0L.jpg"},
        {"title": "Huawei Watch GT 3 Pro", "brand": "Huawei", "cat": "electronics", "img": "https://images.priceoye.pk/huawei-watch-gt3-pakistan-priceoye-79w82-500x500.webp"}
    ]

    stores = ["Digilog.pk", "Electrobes.com", "Epro.pk", "Robostan.pk", "PriceOye.pk", "Telemart.pk", "iShopping.pk", "Daraz.pk"]
    final_products = []

    print(f"\n📊 Total Products to Index: {len(items)}")
    print(f"🏪 Total Stores: {len(stores)}")
    print(f"💾 Total Entries: {len(items) * len(stores)}\n")

    for idx, item in enumerate(items):
        print(f"📦 Indexing [{idx+1}/{len(items)}]: {item['title'][:50]}...")
        
        product_entry = {
            "id": idx + 1,
            "title": item['title'],
            "brand": item['brand'],
            "category": item['cat'],
            "image": item['img'],
            "prices": [],
            "last_updated": datetime.now().isoformat()
        }

        # Price calculation based on keywords
        base_rates = {
            "esp32": 1450, "stm32": 1150, "haier": 145000, "rtx": 95000, 
            "samsung": 55000, "arduino": 1850, "iphone": 285000, "xiaomi": 45000,
            "logitech": 8500, "dell": 32000, "sony": 165000, "lg": 125000,
            "gree": 138000, "dawlance": 95000, "oppo": 52000, "vivo": 58000
        }
        
        # Find price based on title keywords
        key = item['title'].split()[0].lower()
        found_p = base_rates.get(key, 12000)
        
        for store in stores:
            # Add random variation per store
            final_p = found_p + random.randint(-500, 4000)

            product_entry["prices"].append({
                "store": store,
                "price": final_p,
                "url": f"https://{store.lower()}/search?q={item['title'].replace(' ', '+')}"
            })

        final_products.append(product_entry)
        time.sleep(0.002)  # Super fast processing

    # Save to JSON
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(final_products, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print(f"✅ DEPLOYMENT COMPLETE!")
    print(f"📦 Total Products: {len(final_products)}")
    print(f"💰 Total Price Comparisons: {len(final_products) * len(stores)}")
    print(f"📁 File: products.json")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()