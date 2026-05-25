from playwright.sync_api import sync_playwright
import time

ZOMATO_URL = "https://www.zomato.com/mumbai/naturals-ice-cream-YOUR-BRANCH"
PRODUCT_KEYWORD = "coffee crunch"


def check_product_availability():
    print("Opening Zomato...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(ZOMATO_URL, timeout=30000)
            page.wait_for_load_state("networkidle", timeout=20000)
            time.sleep(3)

            page_text = page.inner_text("body").lower()

            if PRODUCT_KEYWORD in page_text:
                if "out of stock" not in page_text:
                    print("Found it and it's in stock!")
                    return True, "Naturals Ice Cream", ZOMATO_URL
                else:
                    print("Found but out of stock.")
                    return False, None, None
            else:
                print("Not found on page.")
                return False, None, None

        except Exception as e:
            print(f"Error: {e}")
            return False, None, None

        finally:
            browser.close()