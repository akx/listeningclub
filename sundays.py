import datetime

this_year = datetime.date.today().year

d = datetime.date(this_year, 1, 1)

while d.year == this_year:
	if d.isoweekday() == 7:
		print(d.isoformat(), "-", "-", "-", sep="\t")
	d += datetime.timedelta(days=1)
