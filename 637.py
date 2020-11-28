

def page(a):
    if a%4 != 0:
        return a + (4 - ( a%4 ))
    else:
        return a

while True:
    page_no = int(input())
    if page_no == 0:
        break
    a = []
    total_page = int(page(page_no))
    sheet = int(total_page/4)
    front = [0 for x in range(2)]
    back = [0 for x in range(2)]

    for n in range(total_page +1):
        if n <= page_no or page_no % 4 == 0 :
            a.append(n)
        else:
            a.append("Blank")

    print("Printing order for {} pages:".format(page_no))

    for sheet_no in range(sheet):
        n = sheet_no * 2 + 1
        front[0] = a[-n]
        front[1] = a[n]
        back [0] = a[n+1]
        back[1] = a[-n-1]

        print("Sheet {}, front: {}, {}".format(sheet_no +1, front[0], front[1]))
        if back[0] != back[1]:
            print("Sheet {}, back : {}, {}".format(sheet_no +1, back[0], back[1]))

