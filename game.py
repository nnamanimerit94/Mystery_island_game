locations = {
    "Beach": {
        "description": """
You are on a Beach
Waves crash against the shore.
A dark jungle looms ahead.

To the north, a dense jungle looms.The air is thick with humidity

You notice a dark lighthouse in the distance on a cliff.
Its beacon is not lit.
        """,
        "exits": {
            "north": "Jungle"
        },
        "items": []
    },

    "Jungle": {
        "description": """
        You are in the jungle, with so much bushes all around, 
        Tall trees that block the rays of the sun and
        a very dark tunnel looms ahead 
        """,
        "exits": {
            "south": "Beach",
            "east": "Cave"
        },
        "items": ["rope"]
    },

    "Cave": {
        'description': """
You're in a dark, cool cave. Water drips from the ceiling,
creating small pools on the ground. The cave is lit by
bioluminescent fungi growing on the walls.

To the west is the jungle. To the east, you can see
an old, rickety bridge spanning a deep gorge.
        """,
        'exits': {
            'west': 'Jungle',
            'east': 'Old Bridge'
        },
        "items": ["lantern"]
    },

    "Old_bridge": {
        'description': """
You stand before an old, rickety rope bridge spanning
a deep gorge. The bridge looks dangerous - some planks
are missing, and the ropes are frayed.

To the west is the cave. The bridge leads east to
the lighthouse, but it looks too dangerous to cross
without proper equipment.
        """,
        'exits': {
            'west': 'Cave',
            'east': 'Lighthouse'  # Will require rope (Checkpoint C)
        },
        "items": []
    },
    'Lighthouse': {
        'description': """
You've reached the lighthouse! It's a tall stone tower
with a large lantern room at the top. The beacon is dark.

Through the windows, you can see the ocean. A rescue
boat is visible in the distance, waiting for the signal.
        """,
        'exits': {
            'west': 'Old Bridge'
        },
        "items": []
    }
}

def get_player_name():
    return input("Enter player name: ").strip()

def display_location(player):
    current_location = player['location']
    location_data = locations[current_location]
    items = location_data['items']


    print("\n Current_Location:", current_location)
    print("-"*50)
    print(location_data['description'])
    if items:
        for item in items:
            print(f"You have {item} to pick up")

def display_menu(player):
    current_location = player['location']
    exits = locations[current_location]['exits']
    items = locations[current_location]['items']

    print("\nWhat would you like to do")

    move_number = 1

    for item in items:
        if len(items)>0:
            print(f"{move_number}. Pick up {item}")
            move_number+=1
            
    for direction, destination in exits.items():
        print(f"{move_number}. Go {direction} to {destination}")
        move_number+=1
        
    print(f"{move_number}. Check inventory")
    print("q. Quit")

def get_choice(exits, items):
    choice_map = {}
    move_number = 1

    for item in items:
        choice_map[str(move_number)] = ('item', item)
        move_number+=1

    for direction in exits.keys():
        choice_map[str(move_number)] = ('direction', direction)
        move_number+=1
    
    return choice_map

def move_player(player, choice_value):
    current_location = player['location']
    exits = locations[current_location]['exits']
    if choice_value in exits:
        if choice_value == 'Old_bridge' and 'rope' not in player['Inventory']:
            print(f"Cannot go to {choice_value} without 'Rope'")
            return False
        elif choice_value == 'Lighthouse' and 'lantern' not in player['Inventory']:
            print(f"Cannot go to {choice_value} without collecting Lantern")
            return False
        else:
            new_location = exits[choice_value]
            player['location'] = new_location
            print(f"\nYou have travelled {choice_value} to {new_location}")
            return True
    else:
        print(f"\nYou can not go {choice_value} from here")
        return False

def pick_up_item(player, choice_value):
    current_location = player['location']
    items = locations[current_location]['items']

    if choice_value in items:
        if choice_value in player['Inventory']:
            print(f"\nYou have collected {choice_value} already")
            return False
        else:
            player['Inventory'].append(choice_value)
            print(f"\nYou have successfully picked up {choice_value}")
            return True
    else:
        print(f"\nYou can not pick up {choice_value} while you are still in {current_location} location")
        return False
