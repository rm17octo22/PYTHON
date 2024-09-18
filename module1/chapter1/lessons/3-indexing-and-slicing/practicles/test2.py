"""
#  Write a Python program to accept a string from the user and display n characters from right of string.

# input

String Slicing in Python
5

"""

# Take the input from the user
str=input()
n=int(input())

# Find the length of the string
l=len(str)

# Find n chars from left of the string
chars = str[l-n::]

# Print the characters
print(chars)

"""
# Write your code here

# Take the input from the user
str=input()
n=int(input())
print(str[19:])

"""