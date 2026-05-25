import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(product_name, store_name, order_link):
    sender   = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    subject = f"Coffee Crunch is IN STOCK at {store_name}!"
    body    = f"Order here: {order_link}"

    msg = MIMEMultipart()
    msg["From"]    = sender
    msg["To"]      = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print("Email sent!")

def send_whatsapp_alert(product_name, store_name, order_link):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
    client.messages.create(
        body=f"ALERT: {product_name} in stock at {store_name}! {order_link}",
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        to=os.getenv("TWILIO_WHATSAPP_TO")
    )
    print("WhatsApp sent!")

def alert_user(product_name, store_name, order_link):
    send_email_alert(product_name, store_name, order_link)
    send_whatsapp_alert(product_name, store_name, order_link)