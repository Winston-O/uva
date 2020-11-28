
while True:
    try:
        case = [int(x) for x in input().split()]
    except EOFError:
        break

    if (case[2] - case[1]) >= case[0]:
        win = 'Props win!'
    else:
        win = 'Hunters win!'
    print(win)
