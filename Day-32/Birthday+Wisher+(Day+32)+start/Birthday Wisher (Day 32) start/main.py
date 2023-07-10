import smtplib
import datetime as dt
import random

'''now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2023:
    print("Don't wear a mask")

date_of_birth = dt.datetime(year=2004, month=6, day=21)
print(date_of_birth)'''

with open("quotes.txt") as file:
    quote_list = file.readlines()
    quote_of_day = quote_list[random.randint(0,102)]
    now = dt.datetime.now()
    day = now.weekday()
    if day == 3:
        my_email = "smiles20004@gmail.com"
        password = "smyceesxzvofaayc"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="builder188@yahoo.com",
                                msg=f"Subject:Motivational Quote\n\n{quote_of_day}")
