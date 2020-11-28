import sys

def read_line():
    return sys.stdin.readline().strip()

for t in range (int(read_line())):
    no_test = int(read_line())
    i = read_line().split()
    N = [int(x) for x in i]
    dist = (max(N) - min(N))*2
    print(int(dist))

