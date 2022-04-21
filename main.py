import smtplib
from datetime import datetime
from random import randint
import pandas

MY_EMAIL = "email@gmail.com"
PASSWORD = "Password"

today = (datetime.now().month, datetime.now().day)

birthday_data = pandas.read_csv("birthdays.csv")

birthday_dict = {(row["month"], row["day"]): row for (index, row) in birthday_data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(f"letter_templates/letter_{randint(1, 3)}.txt") as data:
        contents = data.read()
        new_content = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{new_content}"
        )



