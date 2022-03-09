
import sys

counter = 0
llave_actual = None
val_actual = None

for line in sys.stdin:
        key, val = line.split("\t")
        if key == llave_actual:
                if val != val_actual:
                        counter+=1
        else:
                if llave_actual is not None:
                        print(counter,"\t", "1")
                counter = 1
        llave_actual = key
        val_actual = val
print(counter, "\t", "1")
