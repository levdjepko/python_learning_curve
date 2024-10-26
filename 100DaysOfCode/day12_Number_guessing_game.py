import random

continue_playing = 'y'

while continue_playing == 'y':
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("pick a difficulty - 'easy' or 'hard: ")
    guesses = 0
    if difficulty == 'easy':
        guesses = 10
    else:
        guesses = 5
    print(f"You have {guesses} guesses! ")
    number = random.randint(1, 100)
    for i in range(guesses):
        print("Make a guess!")
        player_guess = int(input())
        if player_guess > number:
            print("Too high!")
        elif player_guess < number:
            print("Too low!")
        elif player_guess == number:
            print("YOU GUESSED CORRECTLY! YOU WON!")
            continue_playing = input("Do you want to do it one more time? :) y or n :")
            break
        guesses -= 1
        print(f"You have {guesses} guesses left")
    if guesses == 0 and continue_playing == 'y':
        print("Sorry, you ran out of guesses!")
        print(f"The number was {number}")
        continue_playing = input("Do you want to do it one more time? :) y or n :")
