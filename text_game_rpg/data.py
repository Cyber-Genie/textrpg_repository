BASE_PLAYER = {

    "health": 10,
    "max_health": 10,
    "stamina": 10,
    "max_stamina": 10,
    "mana": 5,
    "max_mana": 5,
    "gold": 0
}


JOBS = {
    
    "warrior": {
        "title": "Warrior",
        "skills": ["Heavy Strike", "Guard"],
        "description": "A weapon-focused job with strong defensive training."
    },

    "wizard": {
        "title": "Wizard",
        "skills": ["spark", "mana ward"],
        "description": "A magic-focused job with access to early spells." 
    },

    "rogue": {
        "title": "Rogue",
        "skills": ["quick cut", "backstep"],
        "description": "A stamina-focused job with evasive combat skills."
    }
}

ROOMS = {

    "abandoned_shelter": {
        "title": "Abandoned Shelter",
        "description": "Rain taps through holes in the roof. A cold firepit sits in the center of the room, and the door hangs open to the north.",
        "tutorial": True,
        "exits": {
            "north": "forest_crossroad"
        }
    },

     "forest_crossroad": {
        "title": "Forest Crossroad",
        "description": "Three narrow paths cut through the dark trees. The shelter is south, while an old road continues east toward distant lantern light.",
        "tutorial": True,
        "items": ["torch"],
        "exits": {
            "south": "abandoned_shelter",
            "east": "first_town_gate"
        }
    },

    "first_town_gate": {
        "title": "First Town Gate",
        "description": "Lanterns burn above a timber gate. Beyond it waits the first real town, and the road behind you feels colder than before.",
        "tutorial": False,
        "exits": {
            "west": "forest_crossroad"
        }
    }

}

ITEMS = {
    "stamina tonic": {
        "title": "Stamina Tonic",
        "category": "consumables",
        "description": "A bitter drink that restores a small amount of stamina.",
        "usable": True,
        "effect": "restore_stamina",
        "amount": 3
    },

    "old map": {
        "title": "Old Map",
        "category": "utility",
        "description": "A worn map showing a road, a forest, and a town marked with a faded circle.",
        "usable": True,
        "effect": "read"
    },

    "torch": {
        "title": "Torch",
        "category": "utility",
        "description": "An old makeshift torch.",
        "usable": True,
        "effect": "activate_utility"
    }
}