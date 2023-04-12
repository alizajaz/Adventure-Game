# You can use this workspace to write and submit your adventure game project.
import time
import random
import sys


def print_pause(*args):
    for c in args:
        sys.stdout.write(c)
        sys.stdout.flush()
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, ",
                "filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a wicked fairpie is somewhere ",
                "around here,and has been terrifying the nearby village....\n")
    print_pause("In front of you is house.\n")
    print_pause("In your right is dark cave.\n")
    print_pause("In your hand you hold trusty",
                " (but not very effective) dagger.\n")


def user_choice(weapon, m):
    print_pause("Enter 1 to knock the door of the house. \n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do?\n"
                "(Please enter 1 or 2).\n")
    while True:
        place = input()
        if place == "1":
            house(weapon, m)
        elif place == "2":
            cave(weapon, m)
        else:
            validation()


def fight(weapon, m):
    print_pause("You do your best...\n")
    if "sward" in weapon:
        print_pause("As the "+m+" moves to attack,",
                    " you unsheath your new sword.\n")
        print_pause("The Sword of Ogoroth shines brightly in your",
                    " hand as you brace yourself for the attack.\n")
        print_pause("But the "+m+" takes one look at your shiny",
                    " new toy and runs away!\n")
        print_pause("You have rid the town of the "+m+".",
                    " You are victorious!\n")
        print_pause("Would you like to replay (y/n)?\n")
        while True:
            inp1 = input()
            if inp1 == "y":
                play_game()
            elif inp1 == "n":
                print_pause("Thanks for playing, see you next time!\n")
            else:
                validation()
    else:
        print_pause("But your dagger is no match for the "+m+".\n")
        print_pause("You have been defeated!\n")
        print_pause("Would you like to replay (y/n)?\n")
        while True:
            inp2 = input()
            if inp2 == "y":
                play_game()
            elif inp2 == "n":
                print_pause("Thanks for playing, see you next time!\n")
            else:
                validation()


def cave(weapon, m):
    if "sward" in weapon:
        print_pause("You peer cautiously into the cave.\n")
        print_pause("You've been here before, and gotten "
                    "the sword. It's just an empty cave "
                    "now.\n")
        print_pause("You walk back to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.\n")
        print_pause("It turns out to be only a very small cave.\n")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.\n")
        print_pause("You have found the magical Sword of Ogoroth!\n")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.\n")
        print_pause("You walk back out to the field.\n")
        weapon.append("sward")
    user_choice(weapon, m)


def house(weapon, m):
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the doors",
                " open and out steps on the "+m+".\n")
    print_pause("Eep! This is the "+m+"'s house.\n")
    print_pause("The "+m+" attacks you.\n")
    if "sward" in weapon:
        print_pause("You feel confident, because you have",
                    " the magical Sword of Ogoroth!\n")
    else:
        print_pause("You feel under-prepared for this,",
                    " what with only having a tiny dagger.\n")
    print_pause("Would you like to (1) Fight or (2) Run Away?\n")
    while True:
        inp = input()
        if inp == "1":
            fight(weapon, m)
        elif inp == "2":
            print_pause("You run back into the field. Luckily,",
                        " you don't seem to have been followed.\n")
            user_choice(weapon, m)
        else:
            validation()


def validation():
    print_pause("Please make a valid choice!\n")


def play_game():
    weapon = []
    monsters = ["Gorgen", "Troll", "Wicked Witch", "Dragon", "Monster"]
    m = random.choice(monsters)
    intro()
    user_choice(weapon, m)


play_game()
