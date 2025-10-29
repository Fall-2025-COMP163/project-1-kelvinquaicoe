"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kelvin Quaicoe ]
Date: [10/29/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character with initial stats
    Returns: character dictionary
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
    try:
        file = open(filename, 'w')  # Typo
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.close()
        return True
    except Exception as e:
        print(f"Error saving character: {e}")
        return False

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
