count = 0
while True:
    case = [int(x) for x in input().split()]
    if case == [0,0]:
        break
    count += 1
    if case[0] / case[1] > 27:
        ans = 'impossible'
    else:
        if case[0] % case[1] > 0:
            ans = int(case[0] / case[1])
        else:
            ans = int(case[0] / case[1]) - 1

    print("Case {}: {}".format(count, ans))