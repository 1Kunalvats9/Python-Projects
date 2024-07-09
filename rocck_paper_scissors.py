import random
options = ['rock','paper','scissors']

user_wins = 0
computer_wins = 0
while True:
    ask = input("Type Rock/Paper/Scissor to play or Q to quit and S to stop the match: ").lower()
    if ask == 'q':
        print("The user won " + str(user_wins) + " times.")
        print("The computer won " + str(computer_wins) + ' times.')
        if user_wins>computer_wins:
            print("The winner is user")
        elif user_wins<computer_wins:
            print("The winner is computer")
        else:
            print('It is a tie!!')
        
    if ask not in options:
        continue
    random_number = random.randint(0,2)
    # '0' for rocks , '1' for paper , '2' for scissors
    computer_pick =options[random_number]
    print("computer picked " + str(computer_pick) + '.')
    if ask=='rock' and computer_pick=='scissors':
        print("You won!")
        user_wins += 1
    elif ask=='paper' and computer_pick =='rock':
        print('You won!')
        user_wins +=1
    elif ask=='scissor' and computer_pick =='paper':
        print("You won!!")
        user_wins+=1
    else:
        print('Computer won!')
        computer_wins+=1
    