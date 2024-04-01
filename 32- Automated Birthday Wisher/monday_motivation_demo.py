import datetime as dt
import random
import smtplib

import os
import dotenv

dotenv.load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("EMAIL_PASSWORD")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes_data:
        quote_list = quotes_data.readlines()

    random_quote = random.choice(quote_list)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{random_quote}",
        )
