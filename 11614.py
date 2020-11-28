import math
no_test = int(input())
for test in range (no_test):
    c = int(input())
    n = (-1 + math.sqrt(1 + 8 * c)) / 2
    print(int(n))
