# # Welcome the player
# print("=== ESCAPE THE CASTLE ===")
# print("Welcome, adventurer!")

# # # Get information from the player
# # player_name = input("What is your name? ")
# # character_class = input("What type of adventurer are you? ")
# # age = int(input("How old is your character? "))

# # # Set starting values
# # health = 100
# # gold = 20
# # has_key = False

# # # Display the character profile
# # print("\n=== YOUR CHARACTER ===")
# # print(f"Name: {player_name}")
# # print(f"Class: {character_class}")
# # print(f"Age: {age}")
# # print(f"Health: {health}")
# # print(f"Starting gold: {gold}")
# # print(f"Has a key: {has_key}")

# # # Begin the story
# # print(f"\n{player_name}, you wake up in a dark castle.")
# # print("You hear footsteps approaching...")
# # print("Your adventure is about to begin!")

# #region Escape the Castle - Scene 1
# # ==========================================
# # ESCAPE THE CASTLE - SCENE 1: THE CELL
# # ==========================================

# # Introduce the scene to the player
# print("You wake up in a dark castle cell.")
# print("You can see a door, a window and an old bed")

# # Ask the player what they want to investigate
# # .lower() converts their answer to lowercase
# choice = input("Do you want to investigate the door, window or bed?: ").lower()

# # Check whether the player chose the door
# if choice == "door":
#     print("You walk towards the door.")
#     print("You try the handle, but is it locked.")

# # Check whether the player chose the window
# elif choice == "window":
#     print("You look through the window.")
#     print("It is too small to escape through")

# # Check whether the player chose the bed
# elif choice == "bed":
#     print("You look under the bed")
#     print("You find a small Iron Key")

# else: 
#     print("You decide not to investigate")

# #endregion


# #region Escape the Castle - Scene 2
# # ==========================================
# # ESCAPE THE CASTLE - SCENE 2: THE CORRIDOR
# # ==========================================

# # Create a list to store the player's inventory
# # We are assuming the player already found the key
# inventory = ["Iron Key"]


# # Introduce the scene
# print("You enter a long, dark corridor")
# print("You notice an old wooden cabinet")

# choice = input("Do you open the cabinet? yes/no: ")

# if choice == "yes":
#     print("You open the cabinet \nInside, you find a Rusty Dagger!")
  
#     inventory.append("Rusty Dagger")
  
#     print("You pick up the dagger")

# elif choice == "no":
#     print("You leave the cabinet closed.")

# print(f"\n Your Inventory: {inventory}")
# #endregion

#region Escape the Castle - Scene 3



# def encounter(creature):

#     if creature == "guard":
#         print("The Guard draws their sword")
#     elif creature == "ghost":
#         print("The ghost floats towards")
#     elif creature == "draugr":
#         print("the draugr wakes up and slowly walks towards you")

#     print(f"A {creature} appears!!")
    
# encounter("guard")
# encounter("ghost")
# encounter("draugr")

# ==========================================
# ESCAPE THE CASTLE - CORRIDOR ENCOUNTER
# ==========================================

import random

# Define a function to describe an encounter
def encounter(creature):

        # Different outcomes depending on the creature
    if creature == "Guard":
        print("The Guard draws their sword")
    elif creature == "Ghost":
        print("The ghost floats towards")
    elif creature == "Sphinx":
        print("the Sphinx wakes up and slowly walks towards you")

    print(f"A {creature} appears!!")

# Define the corridor scene
def corridor():
    print("You walk down a dark castle corridor.")
    print("You hear a strange noise ahead...")
     # Create a list of possible encounters
    creatures = ["Guard", "Ghost", "Sphinx"]
    
    # Randomly select a creature
    random_creature = random.choice(creatures)

     # Pass the chosen creature into the encounter function
    encounter(random_creature)

# Start the scene
corridor()
#endregion




