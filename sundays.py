import datetime

d = datetime.date(2020, 1, 1)

while d.year == 2020:
	if d.isoweekday() == 7:
		print(d.isoformat())
	d += datetime.timedelta(days=1)