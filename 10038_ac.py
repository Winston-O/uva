import sys

for N in sys.stdin:
    a = N.split()
    if not a:
        break
    seq = [int(x) for x in a[1:]]
    est_max = set(range(1, int(a[0])))
    is_jolly = True
    for i in range (1, len(seq)):
        diff = abs(seq[i-1] - seq[i])
        if diff in est_max:
            est_max.remove(diff)
        else:
            is_jolly = False
            break

    print('Jolly' if is_jolly else 'Not jolly')
















