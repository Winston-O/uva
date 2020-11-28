
import sys

def read_line():
    return sys.stdin.readline()
count = 0
for test in range(int(read_line())):
    uv = {}
    vu = []
    for line in range (10):
        u, v = read_line().split()
        uv.setdefault(int(v), []).append(u)
        vu.append(int(v))
        mv = max(vu)

    count += 1

    print ("Case #{}:".format(count))
    for i in uv.get(mv):
        print(i)