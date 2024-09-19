"""
Print data types of all variables in desired format..

input:
intg = 1452
flot = 11.23
cmplx = 1+2j
booln = True
strng = 'Python'
tpl = (0,-1)
lst = [5,12]
dct = {'class': 'V', 'section': 'A'}

Output:
Type of 1452 is <class 'int'>
Type of 11.23 is <class 'float'>
Type of (1+2j) is <class 'complex'>
Type of True is <class 'bool'>
Type of Python is <class 'str'>
Type of (0, -1) is <class 'tuple'>
Type of [5, 12] is <class 'list'>
Type of {'class': 'V', 'section': 'A'} is <class 'dict'>

"""
intg = 1452
flot = 11.23
cmplx = 1+2j
booln = True
strng = 'Python'
tpl = (0,-1)
lst = [5,12]
dct = {'class': 'V', 'section': 'A'}

print("type of 1452 is " , type(intg))
print("type of 11.23 is ",type(flot))
print("type of (1+2j) is ",type(cmplx))
print("type of booln is ",type(booln))
print("type of 'python' is ",type(strng))
print("type of (0,-1) is ",type(tpl))
print("type of [5,12] is ",type(lst))
print("type of {'class': 'V', 'section': 'A'} is ",type(dct))

#print(type(intg))