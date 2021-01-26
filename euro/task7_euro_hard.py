#! /usr/bin/python3
# original author: Ville Vihtalahti
# I the author grant the use of this code for teaching: yes

# Hard task:
# In the hard task, change your code, so that you can decide the numbers
# you want to play with it. Create a loop so that the game goes on and on,
# until the player wants to exit the game.
# Make it so that the player doesn't accept strings, when asking for numbers.

import random

def my_numbers():
    print("Welcome to the game!")
    eurojackpot_numbers=[]
    for number in range(5):
        while True:
            try:
                number=int(input("Give five different numbers from 1-50 one at a time to begin the game."))
                if number not in eurojackpot_numbers and len(eurojackpot_numbers) <5 and 1<= number <= 50:
                    eurojackpot_numbers.append(number)
                    break
            except ValueError:
                    print("Not one number between 1-50.")
                    continue
            else:
                print("Try again!")
                continue
    
    eurojackpot_numbers=sorted(eurojackpot_numbers)
    print(f"Here are your numbers: {eurojackpot_numbers}")
    my_star_numbers(eurojackpot_numbers)

def my_star_numbers(eurojackpot_numbers):
    star_numbers=[]
    for x in range(2):
        while True:
            try:
                number=int(input("And the star numbers next. Give two different numbers from 1-10 one at a time."))
                if number not in star_numbers and len(star_numbers) <2 and 1 <= number <= 10:
                    star_numbers.append(number)
                    break
            except ValueError:
                    print("Not one number between 1-10.")
                    continue
            else:
                print("Try again!")
                continue

    star_numbers=sorted(star_numbers)
    print(f"Here are all your numbers:{eurojackpot_numbers} {star_numbers}")
    winning_line(eurojackpot_numbers,star_numbers)
    

def winning_line(eurojackpot_numbers, star_numbers):
    winner=random.sample(range(1, 51), 5)
    winner=sorted(winner)
    extra_numbers=random.sample(range(1, 11), 2)
    extra_numbers=sorted(extra_numbers)
    
    your_score=[eurojackpot_numbers for eurojackpot_numbers, winner in zip(eurojackpot_numbers, winner) if eurojackpot_numbers == winner]
    your_star_score=[star_numbers for star_numbers, extra_numbers in zip(star_numbers, extra_numbers) if star_numbers == extra_numbers]
    
    print(f"Here is the winning line: {winner} {extra_numbers}")
    if len(your_score) == 0 and len(your_star_score) == 0:
        print("You got 0 right!")
    elif len(your_score) >= 1 and len(your_star_score) == 0:
        print(f"You got {len(your_score)} right: {your_score} but 0 extra right.")
    elif len(your_score) == 0 and len(your_star_score) >=1:
        print(f"You got 0 normal right, but {len(your_star_score)} extra right: {your_star_score}")
    else:
        print(f"You got {len(your_score)} normal and {len(your_star_score)} extra right: {your_score} and {your_star_score}.")



my_numbers()

while True:
    ask_player=input("Do you want to play again? Type yes to play again and anything else to end the game.")
    if ask_player == "yes":
        my_numbers()
    else:
        break

# Solution:
# I created a nested for/while loop that asks 5 and 2 times for numbers,
# with different functions for them. Then I used Try and Except ValueError,
# to get the loop always repeating if the player answer was not a number.
# I have never used a if-statement so long than in this while loop, but good it worked.
# Then lastly I printed out your numbers and used the same function as in the normal task.
# But with different variables. 
# Then to ask the player if he wants to play again. I use the same kind of solution,
# as in the blackjack game, to call the first function again and repeat,
# the whole process.





