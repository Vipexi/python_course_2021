#! /usr/bin/python3

def ask_number_from_user():
    while True:
        number_from_user = input("Give a number as digit, like 3")
        try:
            int_number_from_user = int(number_from_user)
            return int_number_from_user
        except:
            pass