
import sys

def add_no (a):
    b = [int(x) for x in a]

    if len(b) == 1:
        print (b[0])
    else:
        b = str(sum(b))
        return add_no(b)


for line in sys.stdin:
    N = line.strip()
    if N == '0':
        break
    add_no(N)



