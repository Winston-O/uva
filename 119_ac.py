
import sys

def read():
    return sys.stdin.readline()
t = 0
while True:
    N = read().rstrip()
    if not N:
        break
    log = {}
    value = 0

    for names in read().split():
        log[names] = value

    for group in range (int(N)):
        inpt = read().split()
        n = [int(x) for x in inpt if x.isdigit()]
        gift_name = [x for x in inpt if not x.isdigit()]

        if n[1] != 0:
            log[gift_name[0]] += (-(n[0]) + n[0] % n[1])
            received_money = int((n[0] - n[0] % n[1]) / n[1])
            for receiver in gift_name[1:]:
                log[receiver] += received_money
    if t > 0:
        print("")
    for names, value in log.items():
        print (f"{names} {value}")
    t+=1

