
import sys
count = 0
def read_line():
    return sys.stdin.readline()

for test in range (int(read_line())):
    data = [int(x) for x in read_line().split()]
    N = data[0]
    speed = max(data[1:])
    count += 1

    print ("Case {}: {}".format(count, speed))