
while True:
    try:
        vt_input = [int(x) for x in input().split()]
    except EOFError:
        break
    v = vt_input [0]
    t = vt_input [1]

    if t == 0:
        d = 0
    else:
        d = v * (2*t)

    print (d)