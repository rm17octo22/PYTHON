# Write a Python program to count the repeated word given by user in that string.
"""
Input:
Book Dance Draw Dance is dance for dance paper dance

dance
"""

# Take the input from the user
string = input()
word = input()

# Convert the string to lower case
string_lower = string.lower()

# Count the number of repetitions
cnt = string_lower.count(word)

# Print the count 
print(cnt)