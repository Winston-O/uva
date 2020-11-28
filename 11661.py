while True:
    highway_len = int(input())
    if highway_len == 0:
        break

    N = [x for x in input()]
    z = N.count("Z")
    half = int(len(N)/2)
    r = N.count("R")
    d = N.count("D")
    n = [index for index, value in enumerate(N) if value == "R" or value == "D"]
    a = [x for x in N if x.isalpha()]
    b = 0

    if z > 0:
        print(0)

    else:
        for i in range(1, len(a)):
            if a[i-1] != a[i]:
                c = (n[i]-n[i-1])

                if b == 0:
                    b = c
                elif b > 0 and c < b:
                    b = c
        print(b)


