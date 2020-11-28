while True:
    try:
        troop_no = input()
    except EOFError:
        break
    army =  [int(x) for x in troop_no.split()]
    army.sort()

    print (army[1] - army[0])


