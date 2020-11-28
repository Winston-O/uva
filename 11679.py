
while True:
    bank, debt_no = input().split()
    if bank == "0" and debt_no == "0":
        break
    r = []
    n = [int(x) for x in input().split()]
    for i in n:
        r.append(i)

    a = [0 for _ in range(int(bank)+1)]

    for j in range(int(debt_no)):
        d, c, v = input().split()
        v = int(v)
        d = int(d)
        c = int(c)
        a[d] -= v
        a[c] += v

    del a[0]
    b = True
    for i in range (int(bank)):
        r[i] += a[i]
        if r[i] < 0:
            b = False
            break
    print("S" if b else "N")