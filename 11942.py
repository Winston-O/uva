import sys

test = input()
print ("Lumberjacks:")
for line in sys.stdin:
    N = [int(x) for x in line.split()]
    if not N:
        break
    elif N == sorted(N) or N[::-1] == sorted(N):
        print("Ordered")
    else:
        print("Unordered")