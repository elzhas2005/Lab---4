import datetime
x = datetime.datetime.today()
y = datetime.datetime.today()-datetime.timedelta(days=1)
print(datetime.datetime.timestamp(x)-datetime.datetime.timestamp(y))