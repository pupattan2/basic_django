from datetime import datetime

print datetime.now()
_date = datetime.strptime('2018-02-1 10:19:45', '%Y-%m-%d %H:%M:%S')
print "_date", _date
_new_date = datetime.now() - _date
print _new_date.days
print int(_new_date.total_seconds())