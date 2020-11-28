import sys

min_deg = 360/60
hour_deg = (5/60)*min_deg

def read_line():
    return sys.stdin.readline()

while True:
    H , M = [float(x) for x in read_line().split(":")]
    if H == 0 and M == 0:
        break

    if H < 6:
        hour = ((H-0)*5*min_deg) + (M*hour_deg)
        m =  ((H-0)*5 + 30) + (M*hour_deg/360*60)
        minute = abs(m-M) * min_deg
        total_deg = abs(180 - minute)

    elif H >= 6:
        m = ((H - 0) * 5 - 30) + (M * hour_deg / 360 * 60)
        minute = abs(m - M) * min_deg
        total_deg = abs(180 - minute)

    print("{:.3f}".format(total_deg))



