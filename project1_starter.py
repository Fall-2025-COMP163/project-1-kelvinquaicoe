"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name:[ Kelvin Quaicoe ]
Date: [10/29/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os

def create_character(name, character_class):
    """
    Displays character information in a formatted way
    """
    strength, magic, health = calculate_stats(character_class, 1)
    
    character_dict = {
        "name": name,  
        "class": character_class, 
        "level": 1,
        "strength": strength, 
        "magic": magic, 
        "health": health, 
        "gold": 100 
    }
    
    return character_dict

def calculate_stats(character_class, level):
    """
    Calculates character stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == 'Mage':
        strength = 60 + (level * 1)
        magic = 100 + (level * 5)
        health = 70 + (level * 3)
    elif character_class == 'Warrior':
        strength = 100 + (level * 5)
        magic = 20 + (level * 1)
        health = 90 + (level * 2)
    elif character_class == 'Cleric':
        strength = 30 + (level * 2)
        magic = 100 + (level * 4)  ###leve*4l -> level * 4
        health = 80 + (level * 1)
    elif character_class == 'Rogue':
        strength = 50 + (level * 4)
        magic = 40 + (level * 4)
        health = 90 + (level * 4)
    else:
        strength = 30 + (level * 2)
        magic = 40 + (level * 3)
        health = 50 + (level * 4)
    
    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to a text file
    Returns: True if successful, False otherwise
    """
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False
    with open(filename, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):
        return None
    character = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(": ")
            if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
                character[key.lower()] = int(value)
            elif key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
    return character


def display_character(character):
    """
    Displays character information in a formatted way
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=" * 23)

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character['level'] += 1
    
    # Recalculate stats for the new level
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== RPG Character System ===\n")
    
    # Create a new character
    hero = create_character("Aragorn", "Warrior")
    display_character(hero)
    
    # Save character
    print("\nSaving character...")
    save_character(hero, "aragorn.txt")
    
    # Level up the character
    level_up(hero)
    display_character(hero)
    
    # Save updated character
    save_character(hero, "aragorn.txt")
    
    # Load character from file
    print("\nLoading character from file...")
    loaded_hero = load_character("aragorn.txt")
    if loaded_hero:
        display_character(loaded_hero)
    
    # Test with different classes
    print("\n=== Testing Different Classes ===\n")
    mage = create_character("Gandalf", "Mage")
    display_character(mage)
    
    rogue = create_character("Bilbo", "Rogue")
    display_character(rogue)
    
    cleric = create_character("Elrond", "Cleric")
    display_character(cleric)
