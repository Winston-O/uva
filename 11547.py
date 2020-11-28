test_no = int(input())
for test in range(test_no):
    n = int(input())
    a = int((((((n * 567) / 9) + 7492) * 235) / 47) - 498)
    a = [x for x in str(a)]
    print(a[-2])