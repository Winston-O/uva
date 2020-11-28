test_no = int(input())
for test in range(test_no):
    case = [int(x) for x in input().split()]
    if case[0] > case[1]:
        a = '>'
    elif case [0] < case [1]:
        a = '<'
    else:
        a = '='
    print (a)