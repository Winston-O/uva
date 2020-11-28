count = 0
while True:
    N = input()
    if not N:
        break
    req_no, prop_no = N.split()
    count += 1
    for i in range (int(req_no)):
        req = input()

    a = []
    b = 0
    c = 0
    d = 0
    rmax = 0
    cmin = 0
    for i in range (int(prop_no)):
        prop_name = input()
        a.append(i)
        price, met_no = input().split()
        price = float(price)
        met_no = int(met_no)
        comp_ratio = met_no / int(req_no)
        for j in range (met_no):
            met_req = input()

        class RFP:
            def __init__ (self, name, num, pnum, cnum, cost):
                self.name = name
                self.num = num
                self.pnum = pnum
                self.cnum = cnum
                self.cost = cost

            def compliance(self):
                if self.num == self.pnum:
                    return 1
                else:
                    return 0

        a[i] = RFP(prop_name, int(met_no), int(req_no), comp_ratio, price)
        b += a[i].compliance()

        if i != 0 and a[i].cnum > a[i-1].cnum:
            rmax = a[i].cnum
        elif i != 0 and a[i].cnum == rmax:
            c += 1
        elif i == 0:
            rmax = a[i].cnum


        if i != 0 and a[i].cost < a[i-1].cost:
            cmin = a[i].cost
        elif i == 0:
            cmin = a[i].cost
        elif i != 0 and a[i].cost == cmin:
            d += 1

        print(b)
        if i == int(prop_no)-1:
            for o in range(len(a)):
                if a[o].compliance() == 1 and b == 1:
                    print("RFP #{}\n{}\n".format(count,a[o].name))
                elif b > 1 and a[o].compliance == 1 and a[o].cost == cmin:
                    print("RFP #{}\n{}\n".format(count,a[o].name))

                elif b == 0 and c < 1 and a[o].cnum == rmax:
                    print("RFP #{}\n{}\n".format(count,a[o].name))

                elif b == 0 and c > 1 and a[o].cost == cmin:
                    print ("RFP #{}\n{}\n".format(count, a[o].name))
