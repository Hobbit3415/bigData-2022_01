import sys

curkey = None
curkey_month = None
maximum_sales = 0
maximum_month = 0
maximum_year = 0
curkey_beta = None

for line in sys.stdin:
	key_year, val = line.split("\t")
	val = int(val)
	key_year_4 = key_year[2:6]
	#print(key_year)
	key_month = key_year[10:12]
	#print(key_month)

	if key_year_4 == curkey:
		if val > maximum_sales:
			maximum_sales = val
			maximum_month = key_month
	else:
		if curkey is not None:
			print((curkey,maximum_month), "\t", maximum_sales)
		maximum_month = key_month
		curkey = key_year_4
		curkey_beta = key_year
		maximum_sales = val
print((curkey,maximum_month), "\t", maximum_sales)
