# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def greetings():
    user_name = input("Hello!  What is your name?\n")
    return user_name

def new_story(users_name):
    while True:
        start_story = input(f"Would you like to write a story, {users_name}?\nSelect 'y for yes, or 'n' to exit.\ny/n \n")

        if start_story == 'y':
            print("Once Upon a Time...")
            break
        elif start_story == 'n':
            print(f"Goodbye, {users_name}")
            break
        
        elif user_continue(start_story, users_name):
            print("OKAY")
            break
        
    return start_story

def user_continue(start_story, users_name):
    try:
        if start_story != 'y':
            if start_story != 'n':
                raise ValueError(f"Only y/n can be accepted, you typed {start_story}")
    except ValueError as e:
        print(f"ValueError: Please select either y/n.\n")
        return False
    
    return True

def main():
    users_name = greetings()
    start_new_story = new_story(users_name)

main()