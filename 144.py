def mech(n, b):
    if n == 0:
        return b[::-1]
    else:
        b.append(n)
        n = n-1
        return mech(n,b)


def money(st,ot):  #both []
    scount = 0
    ocount = 0
    coin_out = 0
    ans = []
    while True:
        if sum(st) <= 0:
            break
        #print (st)

        if ocount >= len(ot) and scount < len(st):
            ocount = 0

        elif scount >= len(st) and ocount < len(ot):
            scount = 0

        elif ocount >= len(ot) and scount >= len(st):
            ocount = 0
            scount = 0

        if coin_out == 0:
            coin_out = ot[ocount]
            ocount += 1
        if st[scount] != 0:
            st[scount] -= coin_out
            coin_out = 0

            if st[scount] <= 0:
                ans.append (str(scount + 1))
                coin_out = -st[scount]
                st[scount] = 0


            #elif st[scount] == 0 :
                #ans.append (scount + 1)

        scount += 1

    for i in ans:
        print (i.rjust(3), end = "")


while True:
    N = [int(x) for x in input().split()]
    if N == [0,0]:
        break
    stud_no = N[0]
    mech_lim = N[1]

    stud_acc = [40] * stud_no
    b = []
    coin = (mech(mech_lim, b))
    money (stud_acc , coin)
    print("")




