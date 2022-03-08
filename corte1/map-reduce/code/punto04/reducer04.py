import sys

for line in sys.stdin:
	lla, val, a = line.split("\t")
	val = int(val)
	a = int(a)
	print(lla,"\t",val,"\t",a)
