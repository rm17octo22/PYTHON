"""
Given two lists as inputs,
write a python program to add the elements of the second list on to the first list at the index location 1.

Input:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 20, 30]

"""

# Write your code here

# Take the lists in variable
lst_orig = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_modify=[10, 20, 30]
lst_orig[1:4] = lst_modify [0:3]
print(lst_orig[0:])

"""

# Take the lists in variable
lst_orig = eval(input())
lst_modify=eval(input())
length=len(lst_modify)+1

# Modify the original list
lst_orig[1:length] = lst_modify

# Print the final modified list
print(lst_orig)

"""