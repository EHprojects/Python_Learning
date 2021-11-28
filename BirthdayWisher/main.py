import smtplib
import datetime as dt
import random
import pandas


MY_EMAIL = "your@email.com"
PASSWORD = "password"

# Import Birthday Data
birthdays = pandas.read_csv("birthdays.csv")
print(birthdays)
# birthdays = birthdays.to_dict(orient="series")
# print(birthdays)
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}



# Pick Random Letter

