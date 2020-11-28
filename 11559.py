
import sys

def read_line():
    return sys.stdin.readline()

while True:
    N = [int(x) for x in read_line().split()]
    if not N:
        break
    compare_cost = []
    part_no, budget, hotel_no, week_no = N[0], N[1], N[2], N[3]

    for p in range(hotel_no):
        price = int(read_line())

        bed_no_week = [int(x) for x in read_line().split()]

        cost =  part_no * price

        for i in bed_no_week:
            if i >= part_no and cost <= budget:
                compare_cost.append(cost)


    if len(compare_cost) == 0:
        print ("stay home")
    else:
        min_cost = min(compare_cost)
        print(min_cost)

