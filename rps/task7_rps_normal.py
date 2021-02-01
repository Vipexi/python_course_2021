#! /usr/bin/python3
# original author: Ville Vihtalahti
# I the author grant the use of this code for teaching: yes

# Normal task:
# Make a game of rock paper scissors
# Rock beats scissors, paper beats rock, scissors beats paper.
# Use while loop make the game repeat itself if wanted.
# Use if, elif and else statements for example. 
# Add a counter that adds how many times the game was played, how many ties and
# how many wins player and computer has, during the game and afterwards.

import random

def games_played():
    number_of_games=player_wins+computer_wins+tie
    return number_of_games

player_wins=0
computer_wins=0
tie=0

while True:
    
    player_choice=input("rock, paper or scissors?")
    choice_of_hand=["rock","paper","scissors"]
    computer_choice=random.choice(choice_of_hand)
    
    print(f"The computer chosed: {computer_choice}")
    
    if player_choice in choice_of_hand:
        
        if player_choice == computer_choice:
            print("It's a tie!")
            tie+=1
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
    else:
        print("Not a valid response!")
        continue

    print(f"The player has now won {player_wins} and the computer has won {computer_wins}. The number of ties {tie}.")      
    
    again=input("Do you want to play again? Type yes if you want to play again, otherwise type anything else.")
    
    if again == "yes":
        continue
    else:
        print(f"The game was played {games_played()} times. The player won {player_wins} times, the computer won {computer_wins} times. Number of ties {tie}.")
        break




#Solution:
# First I imported random, because I need it with when the computer choses a handsign by random.
# Then I made three separate global variables that counts the wins for bot player and computer, and tie games.
# Then I made a huge while loop that first asks the player which handsign the player choses from three alternatives.
# Then I made sure that if the player answer was not one of the three alternatives it asks again, until the requirement is satisfied.
# I created a list which holds the answer to make this work and the computer used random.choice to pick one.
# After that I compared the player and computer answers with one another, and printed the outcome.
# Depending on who won the game the counter add +1 after each round.
# Then I created a separate function at the top to get the amount of games by adding all the counters together.
# Then I print the counters after each turn and ask if the player wants to play again, if yes the game begins again,
# and if anything else the game ends and I print all the counters and times played.


