# ************************************ CRUD RULES *******************************************
# ********************* C = CREATE , R = READ , U = UPDATE , D = DELETE  ********************

######################################### CREATE MODE ########################################

# Create a new list object
my_list = list([1, 2, 3])
print("my_list -", my_list)  

# Create a new dictionary object
my_dict = dict({'name': 'John', 'age': 30})
print("my_dict -", my_dict)  

# Create a new set object
my_set = set(['apple', 'banana', 'cherry', 'apple'])
print("my_set -", my_set) 

# Create a new tuple object
my_tuple = tuple((1, 2, 3))
print("my_tuple -", my_tuple)  

# Create a new string object
my_string = str('Hello, world!')
print("my_string -", my_string)  

# Create a new integer object
my_int = int(42)
print("my_int -", my_int)  

# Type casting from str to int
my_string = '42'
my_int = int(my_string)
print("Type casting from str to int:", type(my_string), type(my_int))

# Type casting from set to list
my_set = {1, 2, 3}
my_list = list(my_set)
print("Type casting from set to list:", type(my_set), type(my_list))

###################################### READ MODE ##########################################

