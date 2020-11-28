
import sys
count = 0

def read_line():
    return sys.stdin.readline()

for test in range (int(read_line())):
    wall_no = int(read_line())
    total_hi = 0
    total_lo = 0
    wall_h = [int(x) for x in read_line().split()]

    for i in range(1, len(wall_h)):
        if (wall_no -1) ==0:
            break
        jump = wall_h[i-1]-wall_h[i]
        if jump > 0:
            total_lo += 1
        elif jump < 0:
            total_hi += 1
    count += 1

    print("Case {}: {} {}".format(count, total_hi, total_lo))