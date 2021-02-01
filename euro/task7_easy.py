#! /usr/bin/python3

# original author: Ville Vihtalahti
# I the author grant the use of this code for teaching: yes

# Easy task:
# Import random
# Make your own eurojackpot line using lists.
# Make a program that prints/returns out 5 numbers within a range of 1-50.
# And 2 numbers within a range of 1-10.

import random

def numbers():
    eurojackpot=random.sample(range(1, 51), 5)
    eurojackpot=sorted(eurojackpot)
    print(f"These are your normal numbers: {eurojackpot}")
    return eurojackpot

def extra_numbers():   
    star=random.sample(range(1, 11), 2)
    star=sorted(star)
    print(f"These are your star numbers: {star}")
    return star

numbers()
extra_numbers()

#Original:

"""def numbers():
    eurojackpot=random.sample(range(1, 51), 5)
    eurojackpot=sorted(eurojackpot)
    star=random.sample(range(1, 11), 2)
    star=sorted(star)
    print(f"These are your normal numbers {eurojackpot} and extra {star}.")"""


# Solution:
# First I imported random to be able to make the two random lists
# using random sample and the range of the real Eurojackpot numbers
# Then I used sort, to order both list in a growing order, from smallest to biggest
# Then printed the numbers using f-strings to get the variables nicely placed in to the string.
# The first version I made had the second function called inside the first one, but then I realised that testing,
# Both of the lists wouldn't work out as good while being in one function
# I played my own random numbers in a eurojackpot game. Are you going to ?