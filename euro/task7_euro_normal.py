#! /usr/bin/python3

# Normal task:
# Now that you have your line, lets check how many you got right.
# Make another function that returns the winning numbers and then it checks,
# how many numbers are the same in the game.
# You can use the function you already made

import random

def normal_numbers():
    eurojackpot=random.sample(range(1, 51), 5)
    eurojackpot=sorted(eurojackpot)
    star=random.sample(range(1, 11), 2)
    star=sorted(star)
    print(f"These are your game numbers: {eurojackpot} {star}")
    winning_line(eurojackpot, star)


def winning_line(eurojackpot, star):
    winner=random.sample(range(1, 51), 5)
    winner=sorted(winner)
    extra_numbers=random.sample(range(1, 11), 2)
    extra_numbers=sorted(extra_numbers)
    your_score=[eurojackpot for eurojackpot, winner in zip(eurojackpot, winner) if eurojackpot == winner]
    your_star_score=[star for star, extra_numbers in zip(star, extra_numbers) if star == extra_numbers]
    print(f"Here is the winning line: {winner} {extra_numbers}")
    if len(your_score) == 0 and len(your_star_score) == 0:
        print("You got 0 right!")
    elif len(your_score) >= 1 and len(your_star_score) == 0:
        print(f"You got {len(your_score)} right: {your_score} but 0 extra right.")
    elif len(your_score) == 0 and len(your_star_score) >=1:
        print(f"You got 0 normal right, but {len(your_star_score)} extra right: {your_star_score}")
    else:
        print(f"You got {len(your_score)} normal and {len(your_star_score)} extra right: {your_score} and {your_star_score}.")

normal_numbers()

#Solution:
# Here I also made two separate lists like in the easy task 
# and sorted them the same way.
# I found this line which compares the lists with each other
# I don't understand the code yet myself :D
# Then I printed the results using f strings with different variables
# Used if statements to differentiate based on how many you got right