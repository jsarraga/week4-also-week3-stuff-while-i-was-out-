def show_item(todoitem):
    """ output a formatted todoitem"""
    print("#{} {}:".format(todoitem.pk, todoitem.title))
    print("\t{}".format(todoitem.description))
    statuses = ['incomplete', 'complete']
    print("\tStatus: {}".format(statuses[todoitem.complete]))
    print()


def main_menu():
    """ return 1, 2, 3, 4, 5, 6 or None for bad input """
    print("1. See incomplete items") # has option to select
    print("2. See complete items") # has option to select
    print("3. See all items") # has option to select
    print("4. Create new item") # assume new items are INcomplete
    print("5. Delete item")
    print("6. Quit")
    print()
    print("Your choice: ", end="")
    choice = input().strip()

    try:
        choicenum = int(choice)
    except ValueError:
        return None
    if choicenum < 1 or choicenum > 6:
        return None
    return choicenum


def bad_input():
    print("Bad input.")


def change_status():
    print("Change status (Y/N)? ", end="")
    choice = input().upper().strip()
    if choice == 'Y':
        return True
    return False


def select_item():
    print("Which one? (enter number) ", end="")
    choice = input().strip()
    try:
        choicenum = int(choice)
    except ValueError:
        return None
    return choicenum


def enter_to_continue():
    print("enter to continue... ", end="")
    input()


def goodbye():
    print("Goodbye")


def get_title():
    print("Input title: ", end="")
    return input()


def get_description():
    print("Input description: ", end="")
    return input()
