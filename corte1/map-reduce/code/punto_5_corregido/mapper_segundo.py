import sys
#input = sys.stdin
#next(input)
for line in sys.stdin:
	
	#segunda = line.split(" ")[1]
	primera = line.split("\t")[0]
	#primera_2 = line.split(" ")[1]
	segunda = line.split()[2]
	#segunda = line[16:26]
	print(primera, "\t",segunda)