import schedule
import time
from scraper import check_product_availability
from notifier import alert_user

PRODUCT_NAME = "Coffee Crunch x Bombay Sweet Shop"

already_notified = False

def check_and_notify():
    global already_notified

    print("Checking stock now...")
    is_available, store_name, link = check_product_availability()

    if is_available and not already_notified:
        alert_user(PRODUCT_NAME, store_name, link)
        already_notified = True
        print("Alert sent! Bot keeps watching.")

    elif is_available and already_notified:
        print("Still in stock. Already notified you.")

    else:
        already_notified = False
        print("Not available yet. Trying again soon.")

schedule.every(5).minutes.do(check_and_notify)

print("Bot started! Press Ctrl+C to stop.")
check_and_notify()

while True:
    schedule.run_pending()
    time.sleep(30)