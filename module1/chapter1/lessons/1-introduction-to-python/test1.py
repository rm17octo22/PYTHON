# Write a Python program to calculate your Body Mass Index (BMI).

# Note: Body mass index is a value derived from the mass and height of a person.
# The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms and height in metres. 
# If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range.


height = float(input())
weight = float(input())
print(round(weight /( height * height),100))

"""
# Take the inputs from the user
height = float(input())
weight = float(input())

# Find the BMI
bmi = weight/(height * height)

# Print the output
print(bmi)
"""