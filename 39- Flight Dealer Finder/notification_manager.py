import os
from twilio.rest import Client
import smtplib

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+14065406948"
TWILIO_VERIFIED_NUMBER = os.getenv("PHONE_NUMBER")

my_email = os.getenv("MY_EMAIL")
password = os.getenv("EMAIL_PASSWORD")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_content):
        message = self.client.messages.create(
            body=message_content,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email_content):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=email_content,
            )
