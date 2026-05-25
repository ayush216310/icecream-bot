import requests
import os
from dotenv import load_dotenv

load_dotenv()

SWIGGY_API = "https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=19.2098601&lng=72.8403975&restaurantId=30906&catalog_qa=undefined&submitAction=ENTER"
SWIGGY_URL = "https://www.swiggy.com/city/mumbai/natural-ice-cream-mahavir-nagar-kandivali-west-rest30906"
PRODUCT_KEYWORD = "coffee fudge crunch"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.swiggy.com/",
    "Origin": "https://www.swiggy.com",
    "cookie": os.getenv("SWIGGY_COOKIE", ""),
}


def check_product_availability():
    print("Checking Swiggy API...")
    try:
        response = requests.get(SWIGGY_API, headers=HEADERS, timeout=15)
        print(f"Status code: {response.status_code}")
        print(f"Response preview: {response.text[:200]}")

        data = response.json()
        menu_text = str(data).lower()

        if PRODUCT_KEYWORD in menu_text:
            print("Coffee Fudge Crunch found!")
            return True, "Naturals Ice Cream Kandivali West", SWIGGY_URL
        else:
            print("Not found yet.")
            return False, None, None

    except Exception as e:
        print(f"Error: {e}")
        return False, None, None