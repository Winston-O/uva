
ans = ['You chickened out.', 'You win.', 'You lose.']
while True:
    roundd = int(input())
    if roundd == -1:
        break
    answer = input()
    answer_unique = set(answer)
    guess = input()
    guess_unique = ''
    for g in guess:
        if g not in guess_unique:
            guess_unique += g
    wrong_count = 0
    condition = 0; #0 = chicken, 1 = win, 2 = lose
    for letter in guess_unique:
        if letter in answer_unique:
            answer_unique.remove(letter)
            if len(answer_unique) == 0:
                condition = 1
                break
        else:
            wrong_count += 1
            if wrong_count >= 7:
                condition = 2
                break
    print('Round {}'.format(roundd))
    print(ans[condition])