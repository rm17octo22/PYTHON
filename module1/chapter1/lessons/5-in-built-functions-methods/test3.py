# Write a Python program to remove an item from a tuple.

"""
Input:
a,b,c,d,e,f,g
f

Output:
('a', 'b', 'c', 'd', 'e', 'g')
"""

# Take input from user
tup_input = input()

# Take the item to be removed from user
item = input()

# Split the input and convert into tuple
tup = tuple(tup_input.split(','))

# Convert the tuple into list to be processed
listx = list(tup)

# Remove the item from list
listx.remove(item)

# Convert the list to tuple
tuplex = tuple(listx)

# Print the tuple
print(tuplex)