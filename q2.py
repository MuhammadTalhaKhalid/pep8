import random

def high_low_game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    guess = input('enter H or L')
    if (guess == 'H' or guess == 'h') and num2 > num1:
        print('you win')
    elif (guess == 'L' or guess == 'l') and num2 < num1:
        print('you win')
    else:
        print('You loose')

    print(f'num1 is {num1} and num2 is {num2}')


def rock_paper_scissors():
    human_guess = input('Enter R for Rock, P for paper and S for Scissor')
    system_guess = random.randint(1, 3)
    rps = ''
    if system_guess == 1:
        rps += 'Paper'
    elif system_guess == 2:
        rps += 'Scissor'
    else:
        rps += 'Rock'

    if human_guess == 'R' and rps == 'Scissor':
        print(f'you won Rock beats Scissor')
    elif human_guess == 'P' and rps == 'Rock':
        print(f'you won Paper beats Rock')
    elif human_guess == 'S' and rps == 'Paper':
        print(f'you won Scissors beat paper')


def number_guessing_game():
    l = []
    h_guess = []

    for i in range(3):
        r_num = random.randint(0, 9)
        l.append(r_num)
        my_guess = int(input('enter your number'))
        h_guess.append(my_guess)

    count = 0
    for j in range(3):
        if h_guess[j] in l:
            count += 1

    print(f'human generated numbers are {h_guess} and random generated numbers are {l}.')
    print(f'matching guesses are {count}')


exit = False
while exit == False:
    game = int(input("enter 1,2,3 or 4 "))

    if game == 1:
        high_low_game()
    elif game == 2:
        rock_paper_scissors()
    elif game == 3:
        number_guessing_game()
    elif game == 4:
        print('Game over')
        exit = True
