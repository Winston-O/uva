
test_no = int(input())
for test in range(test_no):
    cmd_no = int(input())
    posi = 0
    move = []
    for n in range(cmd_no):
        cmdin = input().split()

        same_c = [int(x) for x in cmdin if x.isdigit()]
        if cmdin[0] == "LEFT":
            move.append(-1)
        elif cmdin[0] == "RIGHT":
            move.append(1)
        elif cmdin[0] == "SAME":
            move.append(move[same_c[0]-1])

    posi += sum(move)
    print(posi)

