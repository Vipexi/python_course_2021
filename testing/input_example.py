#! /usr/bin/python3

def ask_from_user():
    answer_from_user = input("do you want to continue")
    if answer_from_user == "yes":
        return True
    else:
        return False