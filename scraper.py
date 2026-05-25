import requests
from bs4 import BeautifulSoup

ZOMATO_URL = "https://www.zomato.com/mumbai/natural-ice-cream-kandivali-west"
PRODUCT_KEYWORD = "Coffee Fudge Crunch Ice Cream"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def check_product_availability():
    print("Checking Zomato...")
    try:
        response = requests.get(ZOMATO_URL, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text().lower()

        if PRODUCT_KEYWORD in page_text:
            if "out of stock" not in page_text:
                print("Found and in stock!")
                return True, "Naturals Ice Cream", ZOMATO_URL
            else:
                print("Found but out of stock.")
                return False, None, None
        else:
            print("Not found yet.")
            return False, None, None

    except Exception as e:
        print(f"Error: {e}")
        return False, None, None