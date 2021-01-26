#! /usr/bin/python3
# original author: Ville Vihtalahti
# I the author grant the use of this code for teaching: yes

# Easy task:
# Make your own eurojackpot line.
# Make a program that prints/returns out 5 numbers within a range of 1-50.
# And 2 numbers within a range of 1-10.

import random

def numbers():
    eurojackpot=random.sample(range(1, 51), 5)
    eurojackpot=sorted(eurojackpot)
    star=random.sample(range(1, 11), 2)
    star=sorted(star)
    print(f"These are your game numbers: {eurojackpot} and {star}")
    return eurojackpot

numbers()

# Solution:
# First I imported random to be able to make the two random lists
# using random sample and the range of the real Eurojackpot numbers
# Then I used sort, to order both list in a growing order, from smallest to biggest
# Then printed the numbers using f-strings to get the variables nicely placed in to the string.
# Lastly I called the function.
# I played my own random numbers in a eurojackpot game. Are you going to ?