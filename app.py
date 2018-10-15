# Python Basics
# To run file... python3 file_name.py

# Variables
character_name = "George"
character_age = "70"

# console a set of strings
print("There once wasa a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " +  character_name + ", ")
print("but didn't like being " + character_age + ".")

# Make George all uppercase
print(character_name.upper())

# Don't forget George is still in lowercase
print(character_name.isupper())

# Now it's true
print(character_name.upper().isupper())

# Character length
print(len(character_name))

# Index on a string
print(character_name[0])

# Index function
phrase = "General Assembly"
# should be 0
print(phrase.index("G"))

# Replace function
print(phrase.replace("General", "Specific"))

#  Printing numbers next to strings
my_num = 5
print(str(my_num) + " my favorite number")
