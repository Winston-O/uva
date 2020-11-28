
count = 0

lugg_side = 20

for n in range(int(input())):
    n = [int(x) for x in input().split()]
    count += 1
    if all(num <= 20 for num in n):
        print ("Case {}: good".format(count))
    else:
        print("Case {}: bad".format(count))