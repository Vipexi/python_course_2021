#! /usr/bin/python3
# original author: Ville Vihtalahti
# I the author grant the use of this code for teaching: yes

# Easy task: Build a calculator, which asks the user for a number,
# and calculates the sum of all numbers from 0 to the usergiven input using for loop.
# For example if given number is 5, then the program counts 0+1+2+3+4+5=15
# or 7 0+1+2+3+4+5+6+7=28.

def counter():
   number=int(input("Give a number:"))
   sum_of_numbers = 0
   for i in range(number):
      sum_of_numbers += i
      
   print("The sum was:",sum_of_numbers)

counter()

#OR

def counter2():
   number=int(input("Give a number:"))
   sum_of_numbers = 0
   for i in range(number):
      sum_of_numbers = sum_of_numbers + i
      
   print("The sum was:",sum_of_numbers)

counter2()

# Solution:
# First I asked the user to give an number as an input.
# Then I made a variable that has 0 in it
# Then use for loop for times given by the user.
# +=i makes the counter add the number for each turn inside the variable
# The later example explains better what the +=i does
