import datetime

unix_time = 1620747647

datetime_obj = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_obj,type(datetime_obj))
print(datetime_str,type(datetime_str))