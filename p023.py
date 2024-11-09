
import datetime

birthday = "1993-03-01"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
# print(birthday_date,type(birthday_date))

current_datetime = datetime.datetime.now()
# print(current_datetime,type(current_datetime))

minus_datetime= current_datetime - birthday_date
print(minus_datetime,type(minus_datetime))

print(minus_datetime.days)
print(minus_datetime.days/365)