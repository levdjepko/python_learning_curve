import random

computer_choice =random.choice(['scissors', 'rock', 'paper'])
user_choice = input('Select: rock, paper, or scissors?\n')

if (computer_choice == user_choice):
    print ('Computer picks: ' + computer_choice)
    print ('Tie')
elif ((user_choice == 'rock' and computer_choice == 'scissors') or 
(user_choice == 'paper' and computer_choice == 'rock') or
(user_choice == 'scissors' and computer_choice == 'paper')):
    print ('Computer picks: ' + computer_choice)
    print ('Player wins!')
else:
    print ('Computer picks: ' + computer_choice)
    print ('Computer wins')
