
import sys

for line in sys.stdin:
    N = line[:-1]

    if N =='DONE':
        break
    N = [x.lower() for x in N if x.isalpha()]

    flag = True
    for i in range(0,len(N)):
        flag = N[i] == N[len(N)-1-i]

        if not flag:
            break
    if flag:
        print ("You won't be eaten!")
    else:
        print('Uh oh..')
