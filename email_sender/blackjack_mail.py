#! /usr/bin/python3

import numpy as np
import random
import os
from email_sender import send_email #imported the email_sender.py we used on the lesson.
import datetime
#imported datetime, to get the date and time accurately.

now=datetime.datetime.now() # https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
now=now.strftime("%Y-%m-%d %H:%M:%S") # this begins the start time. I made it into a variable, so I could use
# it on a f-string to call the send_email function
# split hands is not deployd in this version

def make_a_new_deck():
    deck_of_cards = [i for i in range(52)] 
    for i in range(13): 
        for y in range(4): 
            if i <10:
                deck_of_cards[i+y*13] = i+1
            elif i >= 10:
                deck_of_cards[i+y*13] = 10
    random.shuffle(deck_of_cards)
    return deck_of_cards


def draw_card(deck):
    card = deck.pop()
    return card

def calculate_hand(hand):
    sum_of_hand = sum(hand)
    if sum_of_hand <= 11:
        for i in range(len(hand)):
            if hand[i] == 1:
                hand[i] = 11
                break
    elif sum_of_hand > 21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                break
    sum_of_hand = sum(hand)
    return sum_of_hand
    
    
def print_hands(dealer_hand_local, player_hand_local):
    print("Dealer has", dealer_hand_local)
    print("Player has", player_hand_local)

def ask_if_player_wants_card(player_hand_now):
    question = "you have now " + str(player_hand_now)+", do you want another card?"
    answer_local =input(question)
    return answer_local

"""def write_to_file(winner,game_ended):
    file_to_write.write(f"winner,{winner},game_ended,{game_ended}player hand,{player_hand},dealer hand,{dealer_hand}\n")
    try:
        file_to_write = open(filename,"a")
    except:
        print("can not open file")"""

#I was able to create the csv file below, didn't get the results to be stored in there correctly.
#I also didn't manage to attach the file to the email.


"""if __name__ == "__main__": 

    filename ="blackjack_results.csv" 
    try:
        file_to_write = open(filename,"a")

    except:
        print("Cannot open file")"""


# Two integrers which keeps track on how many times the player has won the game and the other how many game has been played

i=0
i2=0

while True:
    deck = make_a_new_deck()
    dealer_hand = []
    player_hand = []
    dealer_hand.append(draw_card(deck))
    player_hand.append(draw_card(deck))
    print(deck)
    while True:
        print_hands(dealer_hand,player_hand)
        answer = ask_if_player_wants_card(player_hand)
        if answer == "yes":
            player_hand.append(draw_card(deck))
            
            if calculate_hand(player_hand) > 21:
                break
        elif answer == "no":
            break
    while True:
        print_hands(dealer_hand,player_hand)
        if calculate_hand(player_hand) > 21:
            i2+=1
            print("you went over, you lose")
            #write_to_file(0,1)
            break
        elif calculate_hand(dealer_hand) < 16:
            dealer_hand.append(draw_card(deck))
            
        elif calculate_hand(dealer_hand) > 21:
            i+=1
            i2+=1
            print("dealer went over, you win")
            #write_to_file(1,0)
            break
            
        elif calculate_hand(dealer_hand) >= calculate_hand(player_hand):
            i2+=1
            print("Dealer wins!")
            #write_to_file(0,2)
            break
        else:
            i+=1
            i2+=1
            print("Player wins!")
            #write_to_file(1,3)
            break
    
    #file_to_write.write(f"player hand {player_hand} dealer hand {dealer_hand}\n")
    

    new_game = input("Do you want a new game, press enter. If you want to end type: no ")
    if new_game == "no":
        wins=i
        games=i2
        after=datetime.datetime.now() #here is after the game time.
        after=after.strftime("%Y-%m-%d %H:%M:%S")
        send_email("Blackmail",f"The game has started {now} and ended at {after}, player has won {wins} times.\n The game has been played {games} times.")
        break