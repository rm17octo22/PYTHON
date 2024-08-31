# Write a Python program to add a key to a dictionary.

"""
Input:
{'name': 'xyz', 'age': 27, 'salary': 50000}
{'manager': 'abc'}

Output:
{'name': 'xyz', 'age': 27, 'salary': 50000, 'manager': 'abc'}

"""

# Write your code here

dct = eval(input())
val = eval(input())
dct.update(val)
print(dct)
