import datetime

d = datetime.date(2010, 1, 1)

while True:
	if d.isoweekday() == 7:
		print(d.isoformat())
	d += datetime.timedelta(days=1)