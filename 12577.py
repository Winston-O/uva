
import sys
count = 0
for line in sys.stdin:
    n = line.split()

    count += 1
    if "*" in n:
        break
    if "Hajj" in n:
        print("Case {}: Hajj-e-Akbar".format(count))
    elif "Umrah" in n:
        print("Case {}: Hajj-e-Asghar".format(count))
