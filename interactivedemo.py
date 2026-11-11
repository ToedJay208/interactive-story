
# Escape the Castle - Day 1

# Welcome the player
print("=== ESCAPE THE CASTLE ===")
print("Welcome, adventurer!")

# # Get information from the player
# player_name = input("What is your name? ")
# character_class = input("What type of adventurer are you? ")
# age = int(input("How old is your character? "))

# # Set starting values
# health = 100
# gold = 20
# has_key = False

# # Display the character profile
# print("\n=== YOUR CHARACTER ===")
# print(f"Name: {player_name}")
# print(f"Class: {character_class}")
# print(f"Age: {age}")
# print(f"Health: {health}")
# print(f"Starting gold: {gold}")
# print(f"Has a key: {has_key}")

# # Begin the story
# print(f"\n{player_name}, you wake up in a dark castle.")
# print("You hear footsteps approaching...")
# print("Your adventure is about to begin!")


# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================

# Introduce the scene to the player
print("You wake up in a dark castle cell.")
print("You can see a door, a window and an old bed")

# Ask the player what they want to investigate
# .lower() converts their answer to lowercase
choice = input("Do you want to investigate the door, window or bed?: ").lower()

# Check whether the player chose the door
if choice == "door":
    print("You walk towards the door.")
    print("You try the handle, but is it locked.")

# Check whether the player chose the window
elif choice == "window":
    print("You look through the window.")
    print("It is too small to escape through")

# Check whether the player chose the bed
elif choice == "bed":
    print("You look under the bed")
    print("You find a small Iron Key")

else: 
    print("You decide not to investigate")


# ==========================================
# ESCAPE THE CASTLE - SCENE 2: THE CORRIDOR
# ==========================================

# Create a list to store the player's inventory
# We are assuming the player already found the key
inventory = ["Iron Key"]


# Introduce the scene
print("You enter a long, dark corridor")
print("You notice an old wooden cabinet")

choice = input("Do you open the cabinet? yes/no: ")

if choice == "yes":
    print("You open the cabinet")
    print("Inside, you find a Rusty Dagger!")
  
    inventory.append("Rusty Dagger")
  
    print("You pick up the dagger")

elif choice == "no":
    print("You leave the cabinet closed.")

print(f"\n Your Inventory: {inventory}")