import requests
from bs4 import BeautifulSoup

NATURALS_URL = "https://order.naturalicecreams.in/order_summary/95b154d8-582f-11f1-900f-7ec616ec9418?ZDX0E=1"
PRODUCT_KEYWORD = "coffee fudge crunch"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

def check_product_availability():
    print("Checking Naturals website...")
    try:
        response = requests.get(NATURALS_URL, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text().lower()

        if PRODUCT_KEYWORD in page_text:
            print("Coffee Fudge Crunch found on Naturals!")
            return True, "Naturals Ice Cream Mahavir Nagar", NATURALS_URL
        else:
            print("Coffee Fudge Crunch not listed yet.")
            return False, None, None

    except Exception as e:
        print(f"Error: {e}")
        return False, None, None