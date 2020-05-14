'''
import sys
def read_line():
    return sys.stdin.readline().strip()
for N in range (int(read_line())):
    n = read_line().split()
    one = ["o", "n", "e"]
    two = ["t", "w", "o"]


    for elem in n:
        i = [x for x in elem]
        if len(i) ==5:
            print(3)
        elif len(set(i) & set(one)) >= 2:
            print (1)
        elif len(set(i) & set(two)) >= 2:
            print (2)


if input == ont, if else be bugged
'''

import sys
one = ["o", "n", "e"]
two = ["t", "w", "o"]
def read_line():
    return sys.stdin.readline().strip()
for N in range (int(read_line())):
    n = read_line()
    if len(n) ==5:
        print(3)
    elif (n[0]==one[0] and n[1]==one[1]) or (n[1]==one[1] and n[2]==one[2]) or (n[0]==one[0] and n[2]==one[2]):
        print(1)
    else:
        print(2)