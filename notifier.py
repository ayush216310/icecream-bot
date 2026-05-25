import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(product_name, store_name, order_link):
    try:
        sender   = os.getenv("EMAIL_SENDER")
        password = os.getenv("EMAIL_PASSWORD")
        receiver = os.getenv("EMAIL_RECEIVER")

        print(f"Sending email from {sender} to {receiver}...")

        subject = f"Coffee Crunch is IN STOCK at {store_name}!"
        body    = f"Order here: {order_link}"

        msg = MIMEMultipart()
        msg["From"]    = sender
        msg["To"]      = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())

    except Exception as e:
        print(f"EMAIL ERROR: {e}")

def send_whatsapp_alert(product_name, store_name, order_link):
    try:
        sid   = os.getenv("TWILIO_SID")
        token = os.getenv("TWILIO_TOKEN")
        from_ = os.getenv("TWILIO_WHATSAPP_FROM")
        to_   = os.getenv("TWILIO_WHATSAPP_TO")

        print(f"Sending WhatsApp from {from_} to {to_}...")
        print(f"Twilio SID starts with: {sid[:6] if sid else 'NOT SET'}")

        client = Client(sid, token)
        client.messages.create(
            body=f"ALERT: {product_name} in stock at {store_name}! {order_link}",
            from_=from_,
            to=to_
        )
        print("WhatsApp sent!")

    except Exception as e:
        print(f"WHATSAPP ERROR: {e}")

def alert_user(product_name, store_name, order_link):
    send_email_alert(product_name, store_name, order_link)
    send_whatsapp_alert(product_name, store_name, order_link)