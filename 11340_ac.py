import sys

def read():
    return sys.stdin.readline().strip()

for test in range (int(read())):
    pair = {}
    for no_paid_char in range (int(read())):
        key, value = read().split()
        pair[key]= int(value)


    sum_pay = 0
    for article in range(int(read())):
            sum_pay += sum([pair.get(char , 0) for char in read()])
    sum_pay /= 100
    print ('{:.2f}$'.format(sum_pay))

