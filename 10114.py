
while True:
    [loan_time, downpay, owe, depre_no] = [float(x) for x in input().split()]
    if loan_time <0:
        break
    m = []
    rate = []
    car_value = owe + downpay
    pay =  owe/loan_time

    for n in range(int(depre_no)):
        a, b = input().split()
        m.append(int(a))
        rate.append(1-float(b))

    c = 0
    d = True
    for i in range (int(loan_time)):
        m.append(m[-1] + 1)
        if not d:
            break
        for j in range (i, m[i+1]):
            car_value *= rate[i]
            #print("{} {} {} {} {}".format(car_value, owe, i, c, rate[i]))
            if car_value < owe:
                owe -= pay
                rate.append(rate[-1])
                c += 1
            else:
                print("{} month".format(c) if c == 1 else "{} months".format(c))
                d = False
                break




