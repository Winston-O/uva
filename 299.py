#least number of swap of 2 adj carriages

def swap(a, b, c):

    while True:
        if b == sorted (b):
            break
        for i in range(a):
            if i + 1 == a:
                break
            else:
                #left_window = b[i]
                #right_window = b[i + 1]
                if b [i] > b [i + 1]:
                    b[i] , b [i + 1] = b[i + 1] , b [i]
                    c += 1

    return c

def bsort(a, b, c):
    for i in range (a-1):
        #print (i)
        for j in range (a - i - 1):
            print (j)
            print(i)
            print(c)
            print(b[j])
            print(b)

            if b [j] > b [j+1] :
                b [j] , b [j + 1] = b [j + 1] , b [j]
                c += 1
    return c



test_case = input().strip()

if test_case.isdigit():
    for test in range (int(test_case)):
        train_len = (input()) #0<=l<=50

        swap_no = 0
        if train_len == 0 :
            order_input = input()
        else:
            current_order = [int(x) for x in input().split()]
            swap_no = bsort(len(current_order), current_order, swap_no)

        print("Optimal train swapping takes {} swaps.".format (swap_no))


