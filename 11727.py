count = 0
test_no = int(input())
for test in range (test_no):
    case = [int(x) for x in input().split()]
    count += 1
    for salary in case:
        if salary != min(case) and salary != max(case):
            print("Case {}: {}".format(count, salary))