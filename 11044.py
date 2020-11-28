import sys

inpt = int(input())
sonar_area = 3*3
for line in sys.stdin:
    N = [int(x) for x in line.split()]
    if not N:
        break

    num_sonar = ((N[0] - (N[0]%3)) * ((N[1] - (N[1]%3))))/sonar_area
    print (int(num_sonar))
