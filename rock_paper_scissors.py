import random

random_pick = random.randint(0,2)
if random_pick == 0:
    computer_choice = 'scissors'
elif random_pick == 1:
    computer_choice = 'rock'
else:
    computer_choice = 'paper'        

user_choice = input('rock, paper, or scissors?\n')

if (computer_choice == user_choice):
    print ('Computer picks: ' + computer_choice)
    print ('Tie')
elif ((user_choice == 'rock' and computer_choice == 'scissors') or 
(user_choice == 'paper' and computer_choice == 'rock') or
(user_choice == 'scissors' and computer_choice == 'paper')):
    print ('Computer picks: ' + computer_choice)
    print ('Player wins!')
elif ((user_choice == 'paper' and computer_choice == 'scissors') or 
(user_choice == 'rock' and computer_choice == 'paper') or
(user_choice == 'scissors' and computer_choice == 'rock')):
    print ('Computer picks: ' + computer_choice)
    print ('Computer wins')   
