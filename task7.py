#! /usr/bin/python3

# Easy task: Build a calculator, which asks the user for a number,
# and calculates the sum of all numbers from 0 to the usergiven input.
# For example if given number is 5, then the program counts 0+1+2+3+4+5=10
# or 7 0+1+2+3+4+5+6+7=21

"""number=int(input("Give a number:"))
sum = 0
for i in range(number):
   sum += i
	
print("The sum was:",sum)

totallaps = int(input("Give a number: "))
totalsum = 0
for i in range(1,totallaps):
    totalsum = totalsum + i

print("The sum was:",totalsum)"""

# Easy task:
# Make your own eurojackpot line.
# Make a program that prints or returns out 5 numbers within a range of 1-50.
# And 2 numbers within a range of 1-10.

"""import random
import math
import statistics

def normal_numbers():
    eurojackpot=random.sample(range(1, 51), 5)
    eurojackpot=sorted(eurojackpot)
    star=random.sample(range(1, 11), 2)
    star=sorted(star)
    print(f"These are your game numbers: {eurojackpot} {star}")
    winning_line(eurojackpot, star)
    return eurojackpot

# Solution:
# I created two separate lists, with random sample.
# I imported random to make the two lists
# Then I used sort, to order both list in a growing order, from smallest to biggest
# Then printed the numbers using f-strings to get the variables nicely in to the string.
# Lastly I called the normal task function, so I could use this two variables insdie the other one too.
# I played my own random numbers in a eurojackpot game. Are you going to ?


# Normal task:
# Now that you have your line, lets check how many you got right.
# Make another function that returns the winning numbers and then it checks,
# how many numbers are the same in the game.
# You can use the function you already made

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

normal_numbers()"""

#Solution:
# Here I also made two separate lists like in the easy task 
# and sorted them the same way.
# I found this line which compares the lists with each other
# I don't understand the code yet myself :D
# Then I printed the results using f strings with different variables
# Used if statements to differentiate based on how many you got right

import random

def my_numbers():
    eurojackpot_numbers=[]
    for x in range(5):
        while True:
            try:
                number=int(input("Give five different numbers from 1-50 one at a time to begin the game."))
                if number not in eurojackpot_numbers and len(eurojackpot_numbers) <5 and 1 <= number <= 50:
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
                number=int(input("Give two different numbers from 1-10 one at a time to begin the for your star numbers."))
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





