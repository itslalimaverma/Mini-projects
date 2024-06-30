import smtplib
import random
import pandas as pd
my_email = "itslalimaverma@gmail.com"
passw = "jkqy fwtd dkzs dqsr"
import datetime as dt
today=dt.datetime.now()
today_tuple=(today.month,today.day)

data=pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents=file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=passw)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")



# import random
#import smtplib
# import pandas as pd
# my_email = "itslalimaverma@gmail.com"
# passw = "jkqy fwtd dkzs dqsr"
# import datetime as dt
# now = dt.datetime.now()
# weekday=now.weekday()
# print(weekday)
# if weekday==5:
#     with open("quotes.txt") as file:
#         data=file.readlines()
#         quote=random.choice(data)
#
#     print(quote)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email,password=passw)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="itslalima@yahoo.com",
#             msg=f"Subject:Monday Motivation\n\n{quote}")



