
money = 0
N = int(input())
for n in range(N):
    n = input().split()
    if len(n)>1:
        amt = int(n[1])
        if n[0] == "donate":
            money += amt
    elif len(n) == 1:
        if n[0] == "report":
            print(money)