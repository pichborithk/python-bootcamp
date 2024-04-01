import pandas
from datetime import datetime
import random
import smtplib
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")


today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()

    contents = contents.replace("[NAME]", birthday_dict[today]["name"])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_dict[today]["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
