
import sys

for line in sys.stdin:
    inpt = [int(x) for x in line.split()]
    wall = inpt[0]
    if wall == 0:
        break
    day = 1
    initial_climb = 0

    while True:
        percent = min(max( ( inpt[3] / 100 * (day-1) ), 0), 1.0)

        climb = inpt[1] - inpt[1]*percent
        day_climb = initial_climb + climb
        slide_climb = day_climb - inpt[2]

        if day_climb > wall:
            print ('success on day',day)
            break
        elif slide_climb < 0 or (day > 1 and initial_climb <= 0):
            print ('failure on day',day)
            break
        elif day_climb > 0 and day_climb <= wall:
            day += 1
            initial_climb = slide_climb
            continue
#print(day, percent, climb, day_climb, slide_climb, initial_climb)






