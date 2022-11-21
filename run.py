# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
import sys
import re


def greetings():
    """
    Request user input's their name.  
    The request will loop until a valid alphabetic name is entered.
    """
    user_name = input("Hello!  What is your name?\n")
    while True:
        if user_name.isalpha():
            break
        else:
            user_name = input("Please type your name. \n")

    return user_name


class Story_bones:
    """
    Define story elements to be called using random.choice() to build stories.
    Lists will be class attributes to enable them be used within class methods.
    """
    beginning = [
        "One fine morning",
        "It was dark and stormy",
        "The sun shone brightly",
        "The birds were singing",
        "I couldn't believe my eyes"]
    character = [
        "Aoife",
        "Shauna",
        "Eoin",
        "Millie",
        "Evie",
        "Lauren",
        "Bailey"]
    verb = ["was singing about",
            "was dancing around",
            "was walking towards",
            "was listening to",
            "was digging for",
            "was cycling around",
            "was skating over",
            "was shouting about",
            "was painting"]
    time_of_day = ["yesterday", "this evening", "tomorrow", "last night"]
    animal = ["a cat", "a rat", "a badger", "a bee", "a bird", "a paraqueet"]
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
            "mountain peak",
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

    quote = [
        "'Remember, brilliant acting runs in your family'",
        "'This is almost finished'",
        "'Lend me your ears'",
        "'A stitch in time, saves nine'"]

    def __init__(self, character, beginning, time_of_day, animal, dice_1,
                 dice_2, dice_3, dice_4, verb, quote, users_name):
        self.character = character
        self.beginning = beginning
        self.time_of_day = time_of_day
        self.animal = animal
        self.dice_1 = dice_1
        self.dice_2 = dice_2
        self.dice_3 = dice_3
        self.dice_4 = dice_4
        self.verb = verb
        self.quote = quote
        self.users_name = users_name

    def story_bricks(self):
        for i in Story_bones.character:
            for i in Story_bones.beginning:
                for i in Story_bones.verb:
                    for i in Story_bones.dice_3:
                        return f"{random.choice(Story_bones.beginning)}, {random.choice(Story_bones.character)} was {random.choice(Story_bones.verb)} a {random.choice(Story_bones.dice_3)} when ...\n"

    def possibility_1(self):
        for i in Story_bones.animal:
            for i in Story_bones.dice_2:
                return f"Option 1: {random.choice(Story_bones.animal)} carrying {random.choice(Story_bones.dice_2)}\n"    

    def possibility_2(self):
        for i in Story_bones.time_of_day:
            for i in Story_bones.dice_1:
                return f"Option 2: they remembered that {random.choice(Story_bones.time_of_day)} the {random.choice(Story_bones.dice_1)}\n"   

    def possibility_3(self):
        for i in Story_bones.animal:
            for i in Story_bones.quote:
                return f"Option 3: suddenly {random.choice(Story_bones.animal)} said {random.choice(Story_bones.quote)}\n"   

# opening_paragraph = Story_bones(random.choice(self.beginning) + ", " + f"{users_name}" + " and a friend, " + random.choice(self.character) + " were " + random.choice(self.verb) + "...\n\n")
# print(opening_paragraph)


def new_story(users_name):
    """
    Invite user to read a story.
    User's answer must be either 'y' for yes or 'n' for no.
    Loop will prompt until valid input is received.
    """
    print(f"Would you like to read a story, {users_name}?")
    while True:
        start_story = input(f"Select 'y for yes, or 'n' to exit.\ny/n \n")

        if start_story == 'y':
            print("\nThen let's begin...\n")
            break
        elif start_story == 'n':
            print(f"Goodbye, {users_name}")
            sys.exit()
            break

        elif user_continue(start_story, users_name):
            # print("OKAY")
            break

    return start_story


def user_continue(start_story, users_name):
    """
    Add exception to return false to a try condition to ensure that only 'y' or 'n' 
    are valid user input. A false condition will prompt new_story() to continue it's 
    loop requesting valid user input.
    """
    try:
        if start_story != 'y':
            if start_story != 'n':
                raise ValueError()
    except ValueError as e:
        print(f"ValueError: Please select either y/n {users_name}.\n")
        return False

    return True

#     opening_paragraph = random.choice(beginning) + ", " + f"{users_name}" + " and a friend, " + random.choice(character) + " were " + random.choice(verb) + "...\n\n"
#     print(opening_paragraph)
#     # return opening_paragraph

# def user_choose_path(story_options, users_name):
#     possibility_1 = f"{users_name}" + "'s pet," + random.choice(animal)
#     + " named Puddles, spotted " + random.choice(dice_2) + " on a " + random.choice(dice_3) + " and ran off."
#     return possibility

def options():
    """
    Create loop inviting user to choose between option 1, 2, or 3 to continue
    randomised story path.  Only user_options() input '1', '2' or '3' are valid input.
    """
    while True:
        user_choice = input("Choose 1, 2 or 3 to continue the story!\n>>>")
        # if user_choice == '1':
        #     print("you chose path 1 which is an interesting short story")
        #     #code to run an interesting short story
        #     break
        # elif user_choice == '2':
        #     print("you chose story path 2 which is an alternative interesting story")
        #     #code to run an alternative interesting story
        #     break
        # elif user_choice == '3':
        #     print("you chose story path 3, a third option of a short story")
        #     #code to run a third option of a short story
        #     break
        if user_choice == '1' or '2' or '3':
            print(f"You chose story path {user_choice} which is a Very interesting story!")
            break
        elif user_options(user_choice):
            break
    return user_choice


def user_options(user_choice):
    """
    Validate that only user input of '1', '2' or '3' will be accepted.
    """
    try:
        if user_choice != '1':
            if user_choice != '2':
                if user_choice != '3':
                    raise ValueError()
    except ValueError as e:
        print(f"ValueError: Choose 1, 2, or 3 to continue the story.\n")
        return False

    return True


def main():
    """
    All application functions are called in this function.
    """
    
    users_name = greetings()
    start_new_story = new_story(users_name)
    # story_options = story_bones(users_name)
    # first_choice = user_choose_path(story_options, users_name)
    opening_paragraph = Story_bones('character', 'beginning', 'time_of_day', 'animal', 'dice_1', 'dice_2', 'dice_3', 'dice_4', 'verb', 'quote', 'users_name')
    print(opening_paragraph.story_bricks())
    option_1 = Story_bones('character', 'beginning', 'time_of_day', 'animal', 'dice_1', 'dice_2', 'dice_3', 'dice_4', 'verb', 'quote','users_name')
    print(option_1.possibility_1())
    option_2 = Story_bones('character', 'beginning', 'time_of_day', 'animal', 'dice_1', 'dice_2', 'dice_3', 'dice_4', 'verb', 'quote','users_name')
    print(option_1.possibility_2())
    option_3 = Story_bones('character', 'beginning', 'time_of_day', 'animal', 'dice_1', 'dice_2', 'dice_3', 'dice_4', 'verb', 'quote','users_name')
    print(option_1.possibility_3())
    userchoices = options()
    print(userchoices)

    # start_new_story = new_story(users_name)   can I put a loop in main() to loop another story?


main()
