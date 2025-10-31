[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21210872&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge


## Read Me Update
Course: COMP 163
Project 1: Character Creator & Saving/Loading
Author: Kelvin Quaicoe
Date: 10/29/25

# Game Concept:
This project is a text based game.
It creates and manages a character by taking in name and class (Mage, warrior, rogue, Clerc)
Class chosen determines your base stats.

# Design Choices
Based on the class chosen the characters get diffent base stats.
Warrior: High strength and rapid Strength growth rate, low magic, high health
Mage: Low strength, high magic and rapid Magic growth rate, medium health
Rogue: low base stats for everything.
Cleric: Medium strength, high magic, high health

#Formulae used
base_strength = class_modifier + (level * growth_rate) 


# Bonus Creative Features
Rogue has a fast growth rate for all stats but starts with low overall statsencouraging loong term progression.

# AI Usage
AI provided assistance throughout the project in both the design and debugging stages. It was helpful in improving code readability by cleaning up indentation and spacing, as well as identifying unnecessary print() statements that were not required for functionality. AI also helped locate typos and diagnose logical and syntactical errors during debugging. In addition, it identified redundant or inefficient sections of code, leading to a cleaner and more optimized implementation. Finally, AI explained the use of os.path.dirname(), clarifying that it is used to extract the directory portion of a file path, which allows the program to verify the existence of a directory before saving files.

# How to Run
Save the program as character_creator.py in your project folder.

Open a terminal or command prompt in the same directory where the file is saved.

Run the program using the command:
python character_creator.py

The program will automatically:
Create sample characters 
Display each character’s stats in a formatted character sheet.
Save and load character information from text files (e.g., aaron.txt).
Demonstrate character leveling and stat updates.

You can also modify the main section to create your own custom characters or test additional class types.

After running, check your project folder to see the saved character files created by the program.





