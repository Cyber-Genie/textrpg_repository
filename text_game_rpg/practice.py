player = {
    "name": "Travelar",
    "health": 20,
    "stamina": 10
}

while True:
    command = input("> ").lower().strip()

    if command == "status":
        print(player)
    
    elif command == "rest":
        player["stamina"] = player["stamina"] +3
        print("You make camp and rest for a while.")
    
    elif command == "quit":
        print("Bye then, Hope to see you soon!")
        break
    
    else:
        print("I dont know that command, try something else.")