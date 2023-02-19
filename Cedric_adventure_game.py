import time


import random


monsters = random.choice(['Dragon', 'Demon', 'Dire-Wolf'])


def print_pause(message):
    print(message)
    time.sleep(2)


items = ["father's sword"]


def intro():
    print_pause("You find yourself standing on a charred battefield,"
                " filled with dead bodies and skeletons.")
    print_pause("Rumor has it that a " + monsters + " lives here."
                " The " + monsters + " is terriying the villagers.")
    print_pause("To your right is a dreary old castle,"
                "to your left, a small cave with a dim light coming through.")
    print_pause("In your hand is your father's old blade."
                " It has grown dull in the passing years.\n")


def choice_1():
    print_pause("You swing open the doors to the castle,"
                " the " + monsters + " who resides\n"
                "in this castle swoops down from the rafts.")
    if "-slayer" in items:
        print_pause("The " + monsters + " shivers"
                    "as he sees your mighty sword")
        print_pause("you start to unsheathe your sword,"
                    " and the " + monsters + " cowers.")
        attacking()
    else:
        print_pause("The " + monsters + " makes it's way down to you,")
        print_pause("it's roar shakes the foundation of the castle.\n")
        combat_decision()


def choice_2():
    print_pause("You slowly creep into the cave\n")
    if "-slayer" in items:
        print_pause("There is nothing left in the cave"
                    "but your father's old sword.")
        print_pause("You walk out of the cave"
                    "and head back to the charred field.")
        battle_field()
    else:
        print_pause("You see in the glimmering light, a large sword."
                    " It's the"
                    " legendary " + monsters + "-slayer sword.")
        print_pause("You grab the majestic sword.")
        items.append("-slayer")
        print_pause("You lay your father's old sword to rest.")
        items.remove("father's sword")
        print_pause("You head back to the charred battlefield.\n")
        battle_field()


def battle_field():
    choices = input("1. Enter the castle.\n"
                    "2. Walk into the creepy cave.\n"
                    "Please select between 1 and 2.\n")
    if choices == "1":
        choice_1()
    elif choices == "2":
        choice_2()
    else:
        print_pause("That is not a valid option, please choose again\n")
        battle_field()


def attacking():
    attack = input("You now have the option to slay"
                   " the " + monsters + ", do you\n"
                   "1. Pierce the " + monsters + "\n"
                   "2. Slice the " + monsters + ".\n")
    if attack == "1":
        print_pause("You pierce the " + monsters + "'s heart"
                    "with your mighty sword")
        print_pause("You are the victor!")
        print_pause("You have slain the mighty " + monsters + "!")
        play_again()
    elif attack == "2":
        print_pause("You slice the " + monsters + "'s head off.")
        print_pause("You are the victor!")
        print_pause("You have slain the mighty " + monsters + "!")
        play_again()
    else:
        print_pause("This is not a valid option, please choose again\n")
        attacking()


def combat_decision():
    fight_or_flight = input("1. Do you choose to fight or,\n"
                            "2. Do you choose to run.\n")
    if fight_or_flight == "1":
        print_pause("As you try to unsheathe your father's sword,")
        print_pause("your hands shiver and in mere seconds"
                    " the " + monsters + " is upon you.")
        print_pause("The " + monsters + " roars at you"
                    " once more with intensity")
        print_pause("as you try to gather yourself,"
                    " the " + monsters + " opens his mouth")
        print_pause("and burns you to death with it's flames.\n")
        print_pause("Game-Over")
        play_again()
    elif fight_or_flight == "2":
        print_pause("You flee back to the charred battlefield.\n")
        battle_field()
    else:
        print_pause("That is not a valid option, please choose again.\n")
        combat_decision()


def play_again():
    play_again = input("Would you like to play again?\n"
                       "yes or no?\n")
    if "no" in play_again:
        print_pause("Game-over,\n"
                    "Thank you for playing")
    elif "yes" in play_again:
        print_pause("Great, prepare for your adventure!\n")
        play_game()


def play_game():
    intro()
    battle_field()


play_game()
