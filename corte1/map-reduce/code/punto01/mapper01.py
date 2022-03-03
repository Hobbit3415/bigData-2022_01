import sys

for line in sys.stdin:
	date = line.split(",")[2]
	year = date.split("-")[0]
	print(year, "\t", 1)


