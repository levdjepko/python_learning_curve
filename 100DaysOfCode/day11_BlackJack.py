# blackjack card scores
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_more = True

while play_more == True:
    print("\n")
    play = input("Do you want to play BlackJack? y or n \n")
    if play == "y":
        play_more = True
    else:
        play_more = False
        break
    players_cards = []
    computers_cards = []

    players_cards.append(random.choice(cards))
    players_cards.append(random.choice(cards))
    computers_cards.append(random.choice(cards))
    computers_cards.append(random.choice(cards))

    print("Your cards are:")
    print(players_cards)
    print("Your score is: ")
    print(sum(players_cards))
    print("Computer's first card is:")
    print(computers_cards[0])


    while input("Do you want to draw another card? y or n \n") == "y":
        players_cards.append(random.choice(cards))
        if sum(computers_cards) < 17:
            computers_cards.append(random.choice(cards))
        print("Your new card is: " + str(players_cards[-1]))
        print("Your current sum is: " + str(sum(players_cards)))
    print("Your final sum is " + str(sum(players_cards)))
    print("Computer's final sum is " + str(sum(computers_cards)))
    if sum(players_cards) > 21:
        print("You lose")
    elif sum(computers_cards) > 21:
        print("You win")
    elif 21 - sum(players_cards) < 21 - sum(computers_cards):
        print("You win")
    elif 21 - sum(players_cards) > 21 - sum(computers_cards):
        print("Computer wins")
    elif 21 - sum(players_cards) == 21 - sum(computers_cards):
        print("Draw")


