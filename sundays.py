import datetime

d = datetime.date(2022, 1, 1)

while d.year == 2022:
	if d.isoweekday() == 7:
		print(d.isoformat(), "-", "-", "-", sep="\t")
	d += datetime.timedelta(days=1)