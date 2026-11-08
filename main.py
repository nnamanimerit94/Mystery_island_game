from game import get_player_name, get_choice, display_location, display_menu, locations

def display_title_and_instruction():
    print("="*50)
    print("The Mystery Island".center(50))
    print("="*50)
    print("""
You wake up on Mystery Island after a storm. 
The lighthouse is dark, the bridge is locked,
you lose energy when you change location,
and a rescue boat will arrive only if you restore the light in the beacon.
    """)



def main():
    display_title_and_instruction()
    player_name= get_player_name()


    player = {
        "name": player_name,
        "location": 'Beach',
        "Energy": 5,
        "Inventory": [],
        "game_over": False,
        "won": False
    }


    while True:

        print(f"\nWelcome to the land of Adventure {player_name}!")

        display_location(player)

        display_menu(player)

        current_exits = locations[player['location']]['exits']

        direction_map = get_choice(current_exits)

        choice = input("\nEnter your choice: ")

        if choice.startswith("q"):
            print(f"Goodbye! {player_name}")
            break

        inventory = str(len(current_exits)+1)
        if choice == inventory:
            if len(player['Inventory']) == 0:
                print("\nInventory: is empty")
                print("You havent collected an item yet")
                continue
            else:
                print(f"\nInventory: {'(, )'.join(player['Inventory'])}")
                continue


        if choice in direction_map:
            direction = direction_map[choice]

            if direction in current_exits:
                new_location = current_exits[direction]
                if new_location in ("Beach", "Jungle", "Cave"):
                    
                player['location'] = new_location
                print(f"You travel {direction} to {current_exits[direction]}")
                continue

            elif direction in
                
        else:
            print("Invalid choice please select the right options")
            
            





        


       
if __name__ == "__main__":
    main()