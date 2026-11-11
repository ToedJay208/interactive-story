
# Escape the Castle - Day 1

# Welcome the player
print("=== ESCAPE THE CASTLE ===")
print("Welcome, adventurer!")

# Get information from the player
player_name = input("What is your name? ")
character_class = input("What type of adventurer are you? ")
age = int(input("How old is your character? "))

# Set starting values
health = 100
gold = 20
has_key = False

# Display the character profile
print("\n=== YOUR CHARACTER ===")
print(f"Name: {player_name}")
print(f"Class: {character_class}")
print(f"Age: {age}")
print(f"Health: {health}")
print(f"Starting gold: {gold}")
print(f"Has a key: {has_key}")

# Begin the story
print(f"\n{player_name}, you wake up in a dark castle.")
print("You hear footsteps approaching...")
print("Your adventure is about to begin!")