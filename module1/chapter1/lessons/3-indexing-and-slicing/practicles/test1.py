"""
Write a Python program to check whether the given strings are palindromes or not. 
Return True otherwise False.

input:
palindrome

"""
# Take the input from the user
s = input()

# Reverse the string and store it in different variable
s == s[::-1]

# Compare the strings to check if palindrome or not
print(s == s[::-1])