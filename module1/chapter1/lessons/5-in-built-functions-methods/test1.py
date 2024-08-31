# Write a Python program to find the length of a set.
"""
Input:
1 2 find look seek

Output:
5
"""

# Take the input from user
sn = input()

# Split the input on blank spaces and convert it into set
set_new=set(sn.split(' '))
#print(set_new)

# Find the length of string
length_set = len(set_new)

# Print the length of set
print(length_set)