"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

The formula for future value with compound interest is FV = P(1 + r/n)^nt. 
FV = the future value;
P = the principal; 
r = the annual interest rate expressed as a decimal; 
n = the number of times interest is paid each year;
t = time in years.

Test Data : amt = 10000, int = 3.5, years = 7 Expected 
Output : 12722.792627665729


input:
10000
3.5
7

output:
12722.792627665729
"""
p =10000
r = 3.5
n = 7
t = 8640

fv = int(p(1 + r/n) ^ (n*t))
print(fv)
