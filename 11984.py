
def C(F):
    return (F - 32) / (9/5)

def F(C):
    return (9/5)*C +32

count = 0


test = int(input())
for i in range(test):
    a, b = input().split()
    a = float(a)
    b = float(b)
    a = C(F(a) + b)
    count += 1
    print("Case {}: {:.2f}".format(count, a))