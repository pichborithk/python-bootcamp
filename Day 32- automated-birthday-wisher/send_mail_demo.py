import smtplib
import os
import dotenv

dotenv.load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("EMAIL_PASSWORD")

# connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="super_popeye1@yahoo.com",
#     msg="Subject:Hello\n\nThis is the body of my email.",
# )
# connection.close()

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="super_popeye1@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email.",
    )
