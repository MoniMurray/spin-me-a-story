# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
import sys

def greetings():
    user_name = input("Hello!  What is your name?\n")
    return user_name

def new_story(users_name):
    print(f"Would you like to write a story, {users_name}?")
    while True:
        start_story = input(f"Select 'y for yes, or 'n' to exit.\ny/n \n")

        if start_story == 'y':
            print("\nThen let's begin...\n")
            break
        elif start_story == 'n':
            # print(f"Goodbye, {users_name}")
            sys.exit()
            break
        
        elif user_continue(start_story, users_name):
            print("OKAY")
            break
        
    return start_story

def user_continue(start_story, users_name):
    try:
        if start_story != 'y':
            if start_story != 'n':
                raise ValueError()
    except ValueError as e:
        print(f"ValueError: Please select either y/n {users_name}.\n")
        return False
    
    return True

def story_bones(users_name):
    character = ["Aoife", "Shauna", "Eoin", "Millie", "Evie", "Lauren"]
    beginning = [
        "One fine morning", 
        "It was dark and stormy", 
        "The sun shone brightly",
        "The birds were singing",
        "I couldn't believe my eyes"]
    time_of_day = ["yesterday", "evening", "tomorrow", "last night"]
    dice_1 = [
        "curious brown monkey", 
        "shiny chalice", 
        "speedometer", 
        "rising sun", 
        "red backpack", 
        "prickly cactus"]
    dice_2 = [
        "peanuts", 
        "dinosaur bones", 
        "a bag of gold", 
        "an igloo", 
        "a spider", 
        "a caterpiller"]
    dice_3 = [
        "jigsaw", 
        "mountain peaks", 
        "pirate's treasure chest", 
        "precious eagle egg", 
        "circus tent", 
        "elephant"]
    dice_4 = [
        "music", 
        "blackbird", 
        "confusion", 
        "an axe", 
        "a ladder", 
        "a telescope"]
    verb = ["singing", 
    "dancing", 
    "walking", 
    "listening", 
    "digging", 
    "cycling", 
    "skating", 
    "shouting", 
    "painting"]

    opening_paragraph = random.choice(beginning) + ", " + f"{users_name}" + " and a friend, " + random.choice(character) + " were " + random.choice(verb) + "...\n\n"
    print(opening_paragraph)
    return opening_paragraph

def main():
    
    users_name = greetings()
    start_new_story = new_story(users_name)
    story_opening = story_bones(users_name)

main()