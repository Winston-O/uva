
N = int(input())
for n in range (N):
    a, b = input().split()
    a = int(a)
    b = int(b)

    c = (a+b)/2
    d = (a-c)
    x = int(c)
    y = int(d)
    if x - c != 0 or y - d != 0 or y < 0:
        print("impossible")
    else:
        print("{} {}".format(x, y))

