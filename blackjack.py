import random

# Possible cards with their respective rates of being drawn
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


# Player Initialization
pA_name = input("Enter your name player 1: ")
pA_score = 0

pB_name = input("Enter your name player 2: ")
pB_score = 0


# Funciton for diplaying the cards
def displayStats():
    print(f"{pA_name} has: {pA_score}")
    print(f"{pB_name} has: {pB_score}")


# BLACKJACK
game = True


#Start of the Game
pA_score += random.choice(cards)
pB_score += random.choice(cards)
displayStats()


pA_inp = input(f"Draw or fold {pA_name}? (1 for draw 0 for fold)\n")
pB_inp = input(f"Draw or fold {pB_name}? (1 for draw 0 for fold)\n")


while game:
    # Get correct input from the user
    if pA_inp not in ["0", "1"]:
        print("Wrong input try again!")
        pA_inp = input(f"Draw or fold {pA_name}? (1 for draw 0 for fold)\n")
        continue
    if pB_inp not in ["0", "1"]:
        print("Wrong input try again!")
        pB_inp = input(f"Draw or fold {pB_name}? (1 for draw 0 for fold)\n")
        continue

    # Draw
    if pA_inp == "1":
        pA_score += random.choice(cards)
    if pB_inp == "1":
        pB_score += random.choice(cards)
    displayStats()

    
    # Case: LOSS
    if pA_score > 21:
        print(f"{pA_name} lost. Cards add up to: {pA_score}")
        game = False
    if pB_score > 21:
        print(f"{pB_name} lost. Cards add up to: {pB_score}")
        game = False

    # Case: GAME OVER
    if pA_inp == "0" and pB_inp == "0":
        if pA_score > pB_score:
            print(f"{pA_name} won with {pA_score}!")
        elif pB_score > pA_score:
            print(f"{pB_name} won with {pB_score}!")
        elif pA_score == 21:
            print(f"{pA_name} won with {pA_score}!")
        elif pB_score == 21:
            print(f"{pB_name} won with {pB_score}!")
        else:
            print("Draw")
        game = False

    
    # Continue to draw
    if pA_inp == "1":
        pA_inp = input(f"Draw or fold {pA_name}? (1 for draw 0 for fold)\n")
    if pB_inp == "1":
        pB_inp = input(f"Draw or fold {pB_name}? (1 for draw 0 for fold)\n")
