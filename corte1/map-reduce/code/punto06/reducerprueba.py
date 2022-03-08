import sys


for line in sys.stdin:
	key,val = line.split("\t")
	print(key,"\t",val)
