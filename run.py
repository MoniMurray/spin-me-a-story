# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def greetings():
    user_name = input("Hello!  What is your name?\n")
    return user_name

def new_story(user_name):
    start_story = input(f"Would you like to write a story, {users_name}?\n Select 'y for yes, or 'n' to exit.  y/n \n")
    if start_story == 'y':
        print("Once Upon a Time...")
    elif start_story == 'n':
        print(f"Goodbye, {users_name}")
    else: 
        print("Please select either y/n.\n")
    return start_story

users_name = greetings()
new_story(users_name)