from game import get_player_name, get_choice, display_location, display_menu, pick_up_item, move_player, locations

def display_title_and_instruction():
    print("="*50)
    print("The Mystery Island".center(50))
    print("="*50)
    print("""
You wake up on Mystery Island after a storm. 
The lighthouse is dark, the bridge is locked,
You lose energy when you change location,
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

        if player["Energy"] == 0:
            player['game_over'] = True
            print("Game over!!!")
            break

        display_location(player)

        display_menu(player)

        exits = locations[player['location']]['exits']
        items = locations[player['location']]['items']

        choice_map = get_choice(exits, items)

        choice = input("\nEnter your choice: ")

        if choice.startswith("q"):
            print(f"Goodbye! {player_name}")
            break

        inventory = str(len(items)+len(exits)+1)
        if choice == inventory:
            print('')
            print("-"*20)
            if len(player['Inventory']) == 0:
                print("Inventory: is empty")
                print("You havent collected an item yet")
                print("-"*20)

                continue
            else:
                print(f"Inventory: {', '.join(player['Inventory'])}")
                print("-"*40)
                continue


        if choice in choice_map:
            choice_type, choice_value = choice_map[choice]

            if choice_type == 'item':
                pick_up_item(player, choice_value)

            elif choice_type == 'direction':
                move_player(player, choice_value)
        else:
            print("Invalid choice please select the right options")

       
if __name__ == "__main__":
    main()