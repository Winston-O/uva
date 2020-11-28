winner = {0: 'A', 1:'B', 2:'C'}

while True:
    try:
        case = [int(x) for x in input().split()]
    except EOFError:
        break

    win = -1
    for no in range (len(case)):
        if case[no] != case[no-1] and case[no] != case[no-2]:
            win = no

    print('*' if win == -1 else winner.get(win))

