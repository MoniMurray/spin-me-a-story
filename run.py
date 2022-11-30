import random   # to select random story components for each story iteration.
import sys   # use to enable user to exit() the application.
import os   # use to clear terminal of previous text to avoid clutter.
os.system('cls' if os.name == 'nt' else 'clear')


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
            user_name = input("Please type your name using only upper"
                              " or lower case letters.\nIntegers and/or"
                              " spaces are not accepted input.\n")

    return user_name


class Story_bones:
    """
    Define story elements to be called using random.choice() to build
    stories.  Lists containing components for a story will be
    class attributes to enable them be used within class methods.
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
            "was painting",
            "was passing by",
            "was looking for",
            "was going for",
            "was cooking"]
    time_of_day = ["yesterday", "this evening", "tomorrow",
                   "last night", "about 100 years ago", "in olden days"]
    animal = ["a cat", "a rat", "a badger", "a bee", "a bird",
              "a paraqueet", "a snail", "a whale"]
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
            "blue elephant"]
    dice_4 = [
            "music",
            "blackbird",
            "confusion",
            "an axe",
            "a ladder",
            "a telescope"]
    dice_5 = [
        "A puzzled Giant, who had lost his glasses,",
        "An old lady, whose shimmering pendant was lost many years before,",
        "The kindly King Crab, who was beloved by his loyal subjects,",
        "A short-sighted Octopus",
        "A powerful wizard, who lived in a palace with"
        " rooftops of shimmering gold,"
    ]

    dice_6 = [
        "a ninja",
        "a pirate",
        "a knight",
        "a scientist",
        "a storyteller",
        "a magician"
    ]

    quote = [
        "'Remember, brilliant acting runs in your family'",
        "'This is almost finished'",
        "'Lend me your ears'",
        "'A stitch in time, saves nine'"]

    def __init__(self, character, beginning, time_of_day, animal,
                 dice_1, dice_2, dice_3, dice_4, dice_5, dice_6, verb, quote,
                 users_name):
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
        """
        Generate random short-story opening line.
        """
        first_line = [(i, j, k, m)
                      for i in Story_bones.character
                      for j in Story_bones.beginning
                      for k in Story_bones.verb
                      for m in Story_bones.dice_3]
        opening = (f"\n{random.choice(Story_bones.beginning)},"
                   f" {random.choice(Story_bones.character)}"
                   f" {random.choice(Story_bones.verb)}\n"
                   f"a {random.choice(Story_bones.dice_3)}"
                   f" when...\n")
        return opening

    def possibility_1(self, users_name):
        """
        Generate random first option path to continue short-story.
        """
        path_1 = [(a, b) for a in Story_bones.animal
                  for b in Story_bones.dice_2]
        return (
                f"1: ...{random.choice(Story_bones.animal)}"
                f" named {users_name}, carrying"
                f" {random.choice(Story_bones.dice_2)},...\n")

    def possibility_2(self, users_name):
        """
        Generate random second option path to continue short-story.
        """
        path_2 = [(day, animal, dice_2, dice_3, dice_1)
                  for day in Story_bones.time_of_day
                  for animal in Story_bones.animal
                  for dice_2 in Story_bones.dice_2
                  for dice_3 in Story_bones.dice_3
                  for dice_1 in Story_bones.dice_1]
        return (f"2: ...I remembered that"
                f" {random.choice(Story_bones.time_of_day)}"
                f" {users_name}'s pet,\n"
                f"     {random.choice(Story_bones.animal)}"
                f" named Puddles, spotted"
                f" {random.choice(Story_bones.dice_2)}"
                f" and...\n")

    def possibility_3(self):
        """
        Generate random third option path to continue short-story.
        """
        path_3 = [(animal, quotation) for animal in Story_bones.animal
                  for quotation in Story_bones.quote]
        return (f"3: ...suddenly,"
                f" {random.choice(Story_bones.animal)} said,"
                f" {random.choice(Story_bones.quote)}...\n")

    def options(self):
        """
        User options to choose next path of story.
        """
        while True:
            user_choice = input("Choose 1, 2 or 3 to continue the story!\n")
            print("*" * 80)
            if user_choice == '1':
                for i in Story_bones.dice_5:
                    for i in Story_bones.dice_6:
                        story = (
                            f"\nThe story continues:\n\n...began to tell"
                            f" a story.\n{random.choice(Story_bones.dice_5)}"
                            f" saw\na very large crowd of people"
                            f" gathered outside the gates\nof the local"
                            f" carnival, where"
                            f" {random.choice(Story_bones.dice_6)}"
                            f" was\ncoming to perform their show.\n"
                            f"A silvery"
                            f" voice behind them said"
                            f"\n{random.choice(Story_bones.quote)},\n"
                            f"which made no sense whatsoever!\n"
                            f"It had all been a dream!!\n")
                break
            elif user_choice == '2':
                for i in Story_bones.quote:
                    for i in Story_bones.dice_6:
                        story = (
                            f"\nThe story continues:\n\n..."
                            f"{random.choice(Story_bones.dice_5)}"
                            f" said:\n'I'm so glad to see you, please"
                            f" stay for tea.'  Afterwards,"
                            f" when\neveryone was full, "
                            f"{random.choice(Story_bones.dice_6)}"
                            f" danced and sang and performed a"
                            f" wonderful show.\nAfter seeing that, it"
                            f" seemed like a sensible idea to play with"
                            f"\n{random.choice(Story_bones.animal)},"
                            f" go home, have a nap, and plan for"
                            f" tomorrow's great adventure.\nAnd oh, "
                            f" what an adventure that was going to be!\n ")
                break
            elif user_choice == '3':
                if user_choice == '3':
                    for i in Story_bones.dice_5:
                        for i in Story_bones.dice_4:
                            for i in Story_bones.animal:
                                story = (
                                    f"\nThe story continues:...\n\n"
                                    f"{random.choice(Story_bones.dice_5)}"
                                    f"\nwhose "
                                    f"{random.choice(Story_bones.dice_4)}"
                                    f" was magical too,\n"
                                    f"showed photographs of"
                                    f" {random.choice(Story_bones.animal)}"
                                    f" riding his first bicycle,\non a"
                                    f" carousel at the fair,\nplaying a"
                                    f" computer game with his father,\n"
                                    f"being hugged and kissed"
                                    f" by his grandmother.\n\nBut, "
                                    f"there was a mystery - because"
                                    f" the house held no\nsign at all"
                                    f" that"
                                    f" {random.choice(Story_bones.animal)}"
                                    f"-boy lived there too!\n")
                break
            elif user_options(user_choice):
                break
        return story


def new_story(users_name):
    """
    Invite user to read a story.
    User's answer must be either 'y' for yes or 'n' for no.
    Loop will prompt until valid input is received.
    """
    print(f"\nWould you like to read a story, {users_name}?\n")
    while True:
        selection = input(f"Select 'y for yes, or 'n' to exit.\ny/n \n")

        if selection == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nThen let's begin at the beginning...\n")
            break
        elif selection == 'n':
            print(f"\nGoodbye, {users_name}.\n")
            sys.exit()
            break

        elif user_continue(selection, users_name):
            break

    return selection


def user_continue(selection, users_name):
    """
    Add exception to return false to a try condition to ensure that
    only 'y' or 'n' are valid user input. A false condition will
    prompt new_story() to continue it's loop requesting valid user
    input.
    """
    try:
        if selection != 'y':
            if selection != 'n':
                raise ValueError()
    except ValueError as e:
        print(f"ValueError: Please select either y/n {users_name}.\n")
        return False

    return True


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


def ending(selection, users_name):
    """
    Get user input to either start another story loop or end and exit.
    """
    print(f"The End.\n\n\nWould you like another story, {users_name}?\n")
    while True:
        selection = input(f"Select 'y for yes, or 'n' to exit.\ny/n \n")

        if selection == 'y':
            break
        elif selection == 'n':
            print(f"Goodbye, {users_name}")
            sys.exit()
            break

        elif user_continue(selection, users_name):
            break

    return selection


def main():
    """
    Run all application functions.
    """
    users_name = greetings()
    selection = new_story(users_name)
    print("*" * 80)
    opening_paragraph = Story_bones(
        'character', 'beginning', 'time_of_day', 'animal',
        'dice_1', 'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6',
        'verb', 'quote', 'users_name')
    print(opening_paragraph.story_bricks())
    print("*" * 80)
    print("\nChoose from one of the following three path options to"
          " continue your story:\n")
    option_1 = Story_bones(
        'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
        'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6', 'verb',
        'quote', 'users_name')
    print(option_1.possibility_1(users_name))
    option_2 = Story_bones(
        'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
        'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6', 'verb',
        'quote', 'users_name')
    print(option_2.possibility_2(users_name))
    option_3 = Story_bones(
        'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
        'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6', 'verb',
        'quote', 'users_name')
    print(option_3.possibility_3())
    userchoices = Story_bones(
            'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
            'dice_2', 'dice_3', 'dice_4', 'verb', 'quote', 'dice_5', 'dice_6',
            'users_name')
    print(userchoices.options())
    print("*" * 80)

    while ending(selection, users_name) == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{users_name}'s New Story\n")
        print("*" * 80)
        opening_paragraph = Story_bones(
            'character', 'beginning', 'time_of_day', 'animal',
            'dice_1', 'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6',
            'verb', 'quote', 'users_name')
        print(opening_paragraph.story_bricks())
        print("*" * 80)
        print("\nChoose one of the following three path options"
              " to continue your story:\n")
        option_1 = Story_bones(
            'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
            'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6', 'verb',
            'quote', 'users_name')
        print(option_1.possibility_1(users_name))
        option_2 = Story_bones(
            'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
            'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6', 'verb',
            'quote', 'users_name')
        print(option_2.possibility_2(users_name))
        option_3 = Story_bones(
            'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
            'dice_2', 'dice_3', 'dice_4', 'dice_5', 'dice_6', 'verb',
            'quote', 'users_name')
        print(option_3.possibility_3())
        print("*" * 80)
        userchoices = Story_bones(
            'character', 'beginning', 'time_of_day', 'animal', 'dice_1',
            'dice_2', 'dice_3', 'dice_4', 'verb', 'quote', 'dice_5', 'dice_6',
            'users_name')
        print(userchoices.options())
        print("*" * 80)

    else:
        sys.exit()


title = "'Spin Me A Story' - an interactive, random story generator\n"
x = title.center(80)
print("*" * 80)
print(x)
print("*" * 80)

main()
