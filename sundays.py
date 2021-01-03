import datetime

d = datetime.date(2021, 1, 1)

while d.year == 2021:
	if d.isoweekday() == 7:
		print(d.isoformat(), "-", "-", "-", sep="\t")
	d += datetime.timedelta(days=1)