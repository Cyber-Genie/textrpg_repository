from data import BASE_PLAYER, JOBS, ROOMS, ITEMS

def create_player(player_name, job_key):
    player = BASE_PLAYER.copy()

    player["name"] = player_name
    player["job"] = job_key
    player["skills"] = JOBS[job_key]["skills"].copy()
    player["inventory"] = {

        "weapons": [],
        "armour": [],
        "consumables": [],
        "scrolls": [],
        "utility": [],
        "quest": []
    }
    player["inventory"]["consumables"].append("stamina tonic")
    player["inventory"]["utility"].append("old map")
    player["location"] = "abandoned_shelter"
    player["picked_up_items"] = []

    return player

def player_has_item(player, item_name):
    for items in player["inventory"].values():
        if item_name in items:
            return True
    return False

def take_item(player, item_name):
    room_key = player["location"]
    room = ROOMS[room_key]
    room_items = room.get("items", [])
    if item_name not in room_items:
        print("That item is not here.")
        return
    if item_name in player["picked_up_items"]:
        print("You already picked that up.")
        return
    item = ITEMS[item_name]
    category = item["category"]
    player["inventory"][category].append(item_name)
    player["picked_up_items"].append(item_name)
    print("You picked up the item.")

def use_item(player, item_name):
    if item_name not in ITEMS:
        print("Item does not exist.")
        return
    
    if not player_has_item(player, item_name):
        print("You dont have that item.")
        return
    
    item = ITEMS[item_name]

    if not item["usable"]:
        print("You cannot use that right now.")
        return

    if item["effect"] == "restore_stamina":
        player["stamina"] = min(player["max_stamina"], player["stamina"] + item["amount"])
        print(f"You use the {item['title']}. Stamina: {player['stamina']}/{player['max_stamina']}")
        player["inventory"]["consumables"].remove(item_name)

    elif item["effect"] == "read":
        print()
        print(item["title"])
        print(item["description"])
        print()

def inspect_item(player, item_name):
    if item_name not in ITEMS:
        print("That item does not exist.")
        return

    if not player_has_item(player, item_name):
        print("You do not have that item.")
        return

    item = ITEMS[item_name]

    print()
    print(item["title"])
    print("Category:", item["category"])
    print(item["description"])

    if "effect" in item:
        print("Effect:", item["effect"])

    if "amount" in item:
        print("Amount:", item["amount"])

    print()


def show_inventory_categories(player):
    print()
    print("Bag")
    print("Gold:", player["gold"])
    print("Categories:")

    for category in player["inventory"]:
        print("-", category)

    print("- return")
    print()

def show_status(player):
    print()
    print(player["name"])
    print("Job:", player["job"])
    print("Health:", player["health"], "/", player["max_health"])
    print("Stamina:", player["stamina"], "/", player["max_stamina"])
    print("Mana:", player["mana"], "/", player["max_mana"])
    print("Gold:", player["gold"])
    print()

def look(player):
    room_key = player["location"]
    room = ROOMS[room_key]

    print()
    print(room["title"])
    print(room["description"])

    room_items = room.get("items", [])
    visible_items = []
    for item in room_items:
        if item not in player["picked_up_items"]:
            visible_items.append(item)
    if visible_items:
        print("Items here:", ", ".join(visible_items))

    exits = room["exits"].keys()
    print("Exits:",", ".join(exits))
    print()

def move_player(player,direction):
    room_key = player["location"]
    room = ROOMS[room_key]
    
    if direction not in room["exits"]:
        print("You cannot go that way.")
        return
    
    if player["stamina"] <= 0:
        print("You are too tired to move.")
        return

    next_room = room["exits"][direction]
    player["location"] = next_room
    player["stamina"] = max(0, player["stamina"] - 1)

    look(player)

def rest(player):
    player["stamina"] = min(player["max_stamina"], player["stamina"] +3)
    print(f"You make camp and rest for a while. Stamina: {player['stamina']}/{player['max_stamina']}")

def show_help():
    print()
    print("Commands:")
    print("- look")
    print("- status")
    print("- rest")
    print("- move north / north / n")
    print("- move south / south / s")
    print("- quit")
    print()

def show_menu():
    print()
    print("Menu:")
    print("- help")
    print("- return")
    print("- quit")
    print()

def parse_command(command):
    command = command.lower().strip()

    shortcuts = {
        "n": "move north",
        "north": "move north",
        "go north": "move north",
        "walk north": "move north",

        "s": "move south",
        "south": "move south",
        "go south": "move south",
        "walk south": "move south",

        "e": "move east",
        "east": "move east",
        "go east": "move east",
        "walk east": "move east",

        "w": "move west",
        "west": "move west",
        "go west": "move west",
        "walk west": "move west",

        "i": "inventory",
        "inv": "inventory",
        "bag": "inventory",
        "pouch": "inventory",

        "stats": "status",
        "hp": "status",

        "speak": "talk",
        "chat": "talk",

        "commands": "help",
        "options": "menu",
        "back": "return",
        "close": "return",
        "leave": "return",

    }

    if command in shortcuts:
        return shortcuts[command]

    if command.startswith("talk to "):
        return command.replace("talk to ", "talk ", 1)

    if command.startswith("speak to "):
        return command.replace("speak to ", "talk ", 1)

    if command.startswith("speak "):
        return command.replace("speak ", "talk ", 1)

    if command.startswith("chat with "):
        return command.replace("chat with ", "talk ", 1)

    if command.startswith("chat "):
        return command.replace("chat ", "talk ", 1)

    if command.startswith("examine "):
        return command.replace("examine ", "inspect ", 1)

    if command.startswith("check "):
        return command.replace("check ", "inspect ", 1)

    if command.startswith("grab "):
        return command.replace("grab ", "take ", 1)

    if command.startswith("pickup "):
        return command.replace("pickup ", "take ", 1)

    if command.startswith("pick up "):
        return command.replace("pick up ", "take ", 1)

    return command
