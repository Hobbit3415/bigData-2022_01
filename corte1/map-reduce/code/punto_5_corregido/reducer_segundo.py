import sys

curkey = None
curkey_year = None
total = 0

for line in sys.stdin:
	key_year, key_month= line.split("\t")
	key_month=int(key_month)

	if key_year == curkey_year:
		total += key_month
	else:
		if (curkey_year) is not None:
			print(curkey_year,"\t", total)
		curkey_year = key_year
		total = key_month
print(curkey_year, "\t", total)