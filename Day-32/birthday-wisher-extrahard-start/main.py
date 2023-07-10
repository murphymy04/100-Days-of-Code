##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
import random

birthday = pd.read_csv("birthdays.csv", index_col=False)
now = dt.datetime.now()
month = now.month
day = now.day
my_email = "smiles20004@gmail.com"
password = "smyceesxzvofaayc"


for i in birthday["month"]:
    if i == month:
        for u in birthday["day"]:
            if u == day:
                row = birthday.loc[birthday["day"] == u]
                name = row["name"].item()
                email = row["email"].item()

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    num = random.randint(0, 3)
                    if num == 0:
                        letter = open("letter_templates/letter_1.txt")
                        lines = letter.readlines()
                        lines[0] = lines[0].replace("[NAME]", name)
                        final_letter = "".join(lines)
                        letter.close()
                    elif num == 1:
                        letter = open("letter_templates/letter_2.txt")
                        lines = letter.readlines()
                        lines[0] = lines[0].replace("[NAME]", name)
                        final_letter = "".join(lines)
                        letter.close()
                    elif num == 2:
                        letter = open("letter_templates/letter_3.txt")
                        lines = letter.readlines()
                        lines[0] = lines[0].replace("[NAME]", name)
                        final_letter = "".join(lines)
                        letter.close()
                    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{final_letter}")
