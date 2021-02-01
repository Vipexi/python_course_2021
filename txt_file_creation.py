#! /usr/bin/python3

# Easy task:
# Create a text file using python. First import OS.
# Then name a textfile and put it inside a variable.
# Use try and except for error handling, if the write to file whent wrong,
# so an exception occured and it prints an error message.
# Then read what is in the file.
# Then add something more to the file on the next line!
# Then read the same file, but only the second line. Import linecache.
# Then create a new text file.
# Then read one letter from the file you created.
# Then add something to the new file using for loop and after every loop use a new line.
# And then close the file.


import linecache
import os

my_file = "my_poem.txt"

try:
    open(my_file ,"w").write("Roses are red and coders are cool!\n")

except:
    print("file saving failed")


my_files_content=open(my_file, "r").read()

print(my_files_content)

open(my_file, "a").write("Python, C# and Javascript, this time I really give a shit!")

my_files_content1=open(my_file,"r").read()

second_line=linecache.getline(my_file, 2)


my_second_file = "a_coders_nightmare.txt"

try:
    open(my_second_file, "w").write("Boo!\n") #Note that you can only save x once!

except:
    print("file saving failed!")

opened=open(my_second_file,"r")

#print(opened)

letter=opened.readline(1)

print(letter)

for x in range(10):
    open(my_second_file, "a").write("This task is rather fun!\n")

the_whole_file=open(my_second_file,"r").read()

with open(my_second_file) as file:
    boo = file.read()

file.close()

print(file.closed)



