import sys

for line in sys.stdin:
	line = line.strip()
	key,val = line.split("\t")
	print('%02d'%int(val), "\t", 1)