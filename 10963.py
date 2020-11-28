import sys

test = int(input())

for case in range (int(test)):
    blank = input()
    W = input()
    g = []
    for n in range(int(W)):
        a, b = [int(x) for x in input().split()]
        c = abs(a-b)
        g.append(c)


    if len(set(g)) == 1:
        print("yes" if case+1 == test else "yes\n")
    else:
        print("no" if case+1 == test else "no\n")
