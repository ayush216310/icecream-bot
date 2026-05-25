from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

ZOMATO_URL     = "https://www.zomato.com/mumbai/natural-ice-cream-kandivali-west"
PRODUCT_KEYWORD = "coffee crunch"

def check_product_availability():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0)")

    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get(ZOMATO_URL)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(3)

        page_text = driver.find_element(By.TAG_NAME, "body").text.lower()

        if PRODUCT_KEYWORD in page_text:
            if "out of stock" not in page_text:
                return True, "Naturals Ice Cream", ZOMATO_URL
        return False, None, None

    except Exception as e:
        print(f"Error: {e}")
        return False, None, None

    finally:
        driver.quit()