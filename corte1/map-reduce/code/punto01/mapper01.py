import sys
cont = 0

for line in sys.stdin:
	if cont == 0:
		cont = 1
	else:
		date = line.split(",")[2]
		year = date.split("-")[0]
		print(year, "\t", 1)


