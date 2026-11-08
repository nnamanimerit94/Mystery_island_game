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
        }
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
        }

    },

    'Cave': {
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
        }
    },
    'Old Bridge': {
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
        }
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
        }
    }
}

def get_player_name():
    return input("Enter player name: ").strip()

def display_location(player):
    current_location = player['location']
    location_data = locations[current_location]

    print("\n Current_Location:", current_location)
    print("-"*50)
    print(location_data['description'])

def display_menu(player):
    current_location = player['location']
    exits = locations[current_location]['exits']

    print("\nWhat would you like to do")

    move_number = 1
    for direction, destination in exits.items():
        print(f"{move_number}. Go {direction} to {destination}")
        move_number+=1
        
    print(f"{move_number}. Check inventory")
    print("q. Quit")

def get_choice(exits):
    direction_map = {}
    move_number = 1

    for direction in exits.keys():
        direction_map[str(move_number)] = direction
        move_number+=1
    
    return direction_map

def add_rope_and_lantern(player):
    print("please select one inventory to pick-up")
    print("rope")
    print("lantern")

    inventory = input("Enter the item need: ")

    if 

