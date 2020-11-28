
a = []
b = []

while True:
    while True:
        N = input().split()
        if N[0] == "#":
            break
        else:
            for i in N:
                c = [x.lower() for x in i]
                c.sort()
                a.append(c)
                b.append(i)
    b.sort()
    for i in b:
        d = [x.lower() for x in i]
        d.sort()
        if a.count(d) == 1:
            print("{}".format(i))
    if N[0] == "#":
        break

