import sys

for test in sys.stdin:
    a, b = test.split()
    a = int(a)
    b = int(b)
    if a == -1 and b == -1:
        break
    c = abs(a-b)

    if  (c) <= (99/2):
        print(c)
    else:
        print(100-c)
