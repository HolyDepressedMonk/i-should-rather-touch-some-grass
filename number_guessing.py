# A number guessing game

import random

user_input_num = int(input('Enter a number between 1 - 10 : '))
computer_num = random.randint(1, 2)

def guess_num(a, b):
    while a < 11:
        if a > b:
            print("Too High.\nWant to Try Again? Type Yes/No")
            play_again = input()
            if play_again.lower() == 'yes': 
                return guess_num(int(input('Enter a number between 1 - 10 : ')), random.randint(1, 2))
            else:
                return 'Good Bye!'            
        elif a < b:
            print("Too Low.\nWant to Try Again? Type Yes/No")
            play_again = input()
            if play_again.lower() == 'yes': 
                return guess_num(int(input('Enter a number between 1 - 10 : ')), random.randint(1, 2))
            else:
                return 'Good Bye!'
        else:
            print("You guessed perfectly.\nWant to Play Again? Type Yes/No")
            play_again = input()
            if play_again.lower() == 'yes': 
                return guess_num(int(input('Enter a number between 1 - 10 : ')), random.randint(1, 2))
            else:
                return 'Good Bye!'

print(guess_num(user_input_num, computer_num))