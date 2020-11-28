
import sys
for test in sys.stdin:
    card = test.split()
    if not card:
        break
    print(max( [int(x) for x in card] ))
