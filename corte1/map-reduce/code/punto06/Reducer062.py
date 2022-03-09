
import sys

llave_actual = None
total = 0

for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == llave_actual:
                total+=val
        else:
                if llave_actual is not None:
                        print('%10d'%int(llave_actual),"\t", total)
                total =val
                llave_actual = key
print('%10d'%int(llave_actual), "\t", total)
