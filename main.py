# coding: utf-8

import smtplib
import random


MY_EMAIL = "**********@gmail.com"
MY_PASSWORD = "***********"

with open("/Users/********/quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Motivation Quote!\n\n{quote}"
    )

