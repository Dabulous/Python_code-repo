# Ask the user for their name
name = input("Please Enter your Name: \n")

# Print a greeting message with the user's name
print("Good morning ,", name)

# Define a list of player names
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Print the first three players in the list
print(players[0:3])

# Print the next three players in the list (offset by 1)
print(players[1:4])

# Print the next three players in the list (offset by 2)
print(players[2:5])

# Print the entire list of players
print(players)

# Define the first and last names of a person
first_name = "John"
last_name = "Doe"

# Combine the first and last names into a full name
full_name = first_name + " " + last_name

# Print a greeting message with the full name (title case)
print("Hello, " + full_name.title() + "!")

# Print a greeting message with the full name (uppercase)
print("Hello, " + full_name.upper() + "!")

# Print a greeting message with the full name (lowercase)
print("Hello, " + full_name.lower() + "!")

# Print the length of the full name
print("the length of your name is " + str(len(full_name)) + "!")

# Check if the full name ends with "Doe"
print(full_name.endswith("Doe"))

# Check if the full name starts with "John"
print(full_name.startswith("John"))

# Find the index of the first occurrence of "o" in the full name
print(full_name.find("o"))