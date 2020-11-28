N = int(input())
for test in range(N):
    n = input().strip()
    a = n.count("M")
    b = n.count("F")

    print("LOOP" if a > 1 and b > 1 and a-b == 0  else "NO LOOP")