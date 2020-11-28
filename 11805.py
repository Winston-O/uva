test_no = int(input())
count = 0
for test in range(test_no):
    case = [int(x) for x in input().split()]
    count += 1
    ball = (case[1] + case[2]) % (case[0])
    if ball == 0:
        ball = case[0]
    print ("Case {}: {}".format(count, ball))