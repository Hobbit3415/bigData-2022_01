import sys

input = sys.stdin
next(input)
for line in sys.stdin:
	county = line.split(",")[8]
	town = line.split(",")[6]
	print((county,town), "\t", 1)