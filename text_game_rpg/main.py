from data import JOBS
from engine import create_player, show_status, look, move_player, rest, parse_command, show_help, show_menu, show_inventory_categories, use_item, inspect_item, take_item

print("Welcome to the rpg")

player_name = input("Name your character: ").strip()

print("Choose your job:")

for job_key, job_data in JOBS.items():
    print(job_key + ": " + job_data["description"])

while True:
    chosen_job = input("> ").lower().strip()

    if chosen_job in JOBS:
        break
    print("That is not a available job, please choose either Warrior, Wizard, or Rogue.")

player = create_player(player_name, chosen_job)

print("Character Created.")
show_status(player)

def open_inventory(player):
    show_inventory_categories(player)

    while True:
        print()
        print("Choose an inventory category.")
        inventory_command = parse_command(input("> "))

        if inventory_command == "return":
            print("Closing bag.")
            return

        elif inventory_command in player["inventory"]:
            print()
            print(inventory_command.title() + ":")

            items = player["inventory"][inventory_command]

            if items:
                for item in items:
                    print("-", item)
            else:
                print("- empty")

        elif inventory_command.startswith("use "):
            item_name = inventory_command.replace("use ", "", 1)
            use_item(player, item_name)
        
        elif inventory_command.startswith("inspect "):
            item_name = inventory_command.replace("inspect ", "", 1)
            inspect_item(player, item_name)

        else:
            print("That is not an inventory category.")

def open_menu():
    show_menu()

    while True:
        print()
        print("Choose a menu option.")
        menu_command = parse_command(input("menu> "))

        if menu_command == "help":
            show_help()

        elif menu_command == "quit":
            print("Bye, See you next time")
            return "quit"

        elif menu_command == "return":
            print("Returning to game.")
            return "return"

        else:
            print("That is not a menu option.")


while True:
    print()
    print("What do you do?")
    command = parse_command(input("> "))

    if command == "status":
        show_status(player)

    elif command == "inventory":
        open_inventory(player)

    elif command == "look":
        look(player)
    
    elif command.startswith("take "):
        item_name = command.replace("take ", "", 1)
        take_item(player, item_name)

    elif command == "rest":
        rest(player)

    elif command.startswith("move "):
        direction = command.replace("move ", "")
        move_player(player, direction)

    elif command == "menu":
        menu_result = open_menu()
        if menu_result == "quit":
            break

    else:
        print("Unknown Command.")