
v_dict = {"a":1 ,"b":2, "c":3, "d":4, "e":5,
          "f":6, "g":7, "h":8, "i":9, "j":10,
          "k":11, "l":12, "m":13, "n":14, "o":15,
          "p":16, "q":17, "r":18, "s":19, "t":20,
          "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

def add_no(a):
    b = [int(x) for x in a]
    if len(b) == 1:
        return int(b[0])

    else:
        b = str(sum(b))
        return add_no(b)

while True:
    try:
        a = []
        for N in range(2):
            N = input()
            s = str(sum([v_dict.get(x.lower()) for x in N if x.isalpha()]))
            a.append(add_no(s))

            if len(a) == 2:
                a.sort()
                ans = (a[0]/a[1])*100
                print("{:.2f} %".format(ans))
                break
    except EOFError:
        break
