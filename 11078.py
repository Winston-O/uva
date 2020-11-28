
test_no = int(input())
for test in range(test_no):
    case_no = int(input())

    max_diff = maxv = -float('inf')
    for case in range(case_no):
        scores = int(input())
        max_diff  = max(max_diff, maxv-scores)

        maxv = max(maxv, scores)

    print(max_diff)


