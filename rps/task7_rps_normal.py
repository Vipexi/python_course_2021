#! /usr/bin/python3
# original author: Ville Vihtalahti
# I the author grant the use of this code for teaching: yes

# Normal task:
# Make a game of rock paper scissors
# Rock beats scissors, paper beats rock, scissors beats paper.
# Use while loop make the game repeat itself if wanted.
# Use if, elif and else statements for example. 
# Add a counter that adds how many times computer and the player have each won
# and prints the times the player and computer each have won the game

import random

player_wins=0
computer_wins=0


while True:
    choices=["rock","paper", "scissors"]
    player_choice=input("Rock, paper or scissors?")
    computer_choice=random.choice(choices)
    if player_choice not in choices:
        print("Not a valid respons")
        continue
    print(f"The computer chosed: {computer_choice}")
    if player_choice in choices:

        if player_choice == computer_choice:
            print("It's a tie!")
        if player_choice == "rock" and computer_choice == "paper":
            print("Computer wins!")
            computer_wins+=1
        if player_choice == "rock" and computer_choice == "scissors":
            print("Player wins!")
            player_wins+=1
        if player_choice == "paper" and computer_choice == "rock":
            print("Player wins!")
            player_wins+=1
        if player_choice == "paper" and  computer_choice == "scissors":
            print("Computer wins!")
            computer_wins+=1
        if player_choice == "scissors" and computer_choice == "rock":
            print("Computer wins!")
            computer_wins+=1
        if player_choice == "scissors" and computer_choice == "paper":
            print("Player wins!")
            player_wins+=1
        print(f"The player has now won {player_wins} and the computer has won {computer_wins}.")

    again=input("Do you want to play again? Type yes if you want to play again, otherwise type anything else.")
    if again == "yes":
        continue
    else:
        print("Bye!")
        break

            

        




