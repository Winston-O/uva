


N = int(input())
for code in range(N):
    code = input()
    if code in ["1", "4", "78"]:
        print("+")
    elif code[-2:] == "35" and len(code)>2:
        print("-")
    elif code[0] == "9" and code[-1] == "4" and len(code)>2:
        print("*")
    elif code[:3]  == "190" and len(code)>3:
        print("?")


