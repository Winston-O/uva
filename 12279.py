
count = 0
while True:
    N = int(input())
    a = 0
    if N == 0:
        break

    reason = 0
    treat = 0

    while a == 0:

        n = input().split()
        for i in n:
            if i == "0":
                treat +=1
            else:
                reason +=1


        balance = reason - treat


        if len(n) == N:
            a = 1
        count += 1
    print("Case {}: {}".format(count, balance))

