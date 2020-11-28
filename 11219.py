

test_case = int(input())
for test in range (test_case):
    blank = input()
    current = [int(x) for x in input().split("/")]
    birth = [int(x) for x in input().split("/")]

    age = 0

    if birth [2] > current[2] or \
        (birth [2]==current[2] and birth [1] > current[1]) or \
        (birth[2]==current[2] and birth[1]==current[1] and birth[0] > current[0]):
        age = "Invalid birth date"

    elif current [2] > birth [2] and current [2] - birth [2] > 131:
        age = "Check birth date"

    elif current [2] > birth [2] and current [2] - birth [2] == 131 and current [1] > birth [1]:
        age =  "Check birth date"

    elif current [2] > birth [2] and current [2] - birth [2] == 131 and current [1] == birth [1] and current[0] >= birth[0]:
        age = "Check birth date"

    elif current [2] > birth [2] and current [1] > birth [1]:
        age = current[2] - birth [2]

    elif current [2] > birth [2] and current [1] == birth [1] and current [0] >= birth [0]:
        age = current [2] - birth [2]

    elif current [2] > birth [2] and current [1] < birth [1] and current [0] <= birth [0]:
        age = current [2] - birth [2] - 1

    elif current [2] > birth [2] and current [1] < birth [1] and current [0] > birth [0] :
        age = current [2] - birth [2] - 1

    elif current [2] > birth [2] and current [1] == birth [1] and current [0] < birth [0] :
        age = current [2] - birth [2] - 1

    elif current [2] == birth [2] and current [1] == birth [1] and current [0] == birth [0] :
        age = 0



    print("Case #{}: {}".format(test+1, age))