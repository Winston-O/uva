
while True:
    km = input()
    if km.strip() == '0':
        break
    K, M = km.split()
    K = int(K)
    selected_courses = []
    while True:
        selected_courses += input().split()
        if len(selected_courses) >= K:
            break
    selected_courses = set(selected_courses)
    M = int(M)
    flag = True
    for m in range(M):
        C = input().split()
        req = int(C[1])
        contains = set([x for x in C[2:]])
        for sc in selected_courses:
            if sc in contains:
                req -= 1
        flag = flag and req <= 0
    print('yes' if flag else 'no')
