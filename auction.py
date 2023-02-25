import os
from time import sleep

#Create a empyt dictionary for players
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                       !!! AUCTION !!!
'''

Auctions = {}


#Compare bids inside of the dictionary 
def add_player(Auctions):
    highest_bid= 0
    winner = "" 
    for key in Auctions:
        money = Auctions[key]
        if money > highest_bid:
            highest_bid = money
            winner = key
    print(f"The winner of the Auction is {winner} with a bid of £{highest_bid}")
    
#Recieve name and bid inputs untill no more players 
Game = True
print(logo)
while Game != False:
    player = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    Auctions[player]=bid
    Add = input("Is there any other players? ('yes' or 'no')")
    if Add == "yes":
        print("Screen will clear in 2 seconds . . .")
        sleep(2)
        os.system('clear')
        
    else:
        Game = False
        add_player(Auctions)
        
