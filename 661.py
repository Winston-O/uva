count = 0
while True:
    dev_no, op_no, fuse_cap = input().split()
    if dev_no == op_no == fuse_cap == "0":
        break
    max_a = 0
    b = []
    o_f = [0 for x in range (int(dev_no))]
    bomb = False
    count += 1
    for i in range(int(dev_no)):
        a = int(input())
        b.append(a)

    for i in range(int(op_no)):
        n = int(input())
        if o_f [n-1] == 0:
            o_f [n-1] += b[n-1]
            if sum(o_f) > max_a:
                max_a = sum(o_f)
            if max_a > int(fuse_cap):
                bomb = True

        else:
            o_f [n-1] -= b[n-1]

    print("Sequence {}\n"
                      "Fuse was blown.\n".format(count) if bomb else
                      "Sequence {}\n"
                        "Fuse was not blown.\n"
                            "Maximal power consumption was {} amperes.\n".format(count, max_a))