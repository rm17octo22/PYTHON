# datatypes
# .....  int,float,boolean,str,list,tuple,dictionary,set .....
# premitive datatypes :- int ,float ,boolean
# non-premitive data-types :- str, list ,tuple, dictionary, set

#int
integer = 123
print("integer : " ,integer)
print(type(integer))
print('')

#float
float12 = 23.43
print("float :",float12)
print(type(float12))
print('')

#boolean
#return :- True / False
# yes/no , on/off , yes/no , 1/0 
boolean12 = True
boolean1212 = False
print(boolean12)
print(boolean1212)
print(type(boolean12)
      
#str
#immutable
#ordered/indexed
string = "ravi"
print("string :",string)
print(type(string))
print(len(string))
print(string.count('av'))
print('i\'m fine.')
print("""
        hello,
      monika what are you doing???
     """)
print("")

#list
#mutable
#ordered/indexed
#repeated allowed
# accept all dat-type
my_list = ([1,23.4,'ravi'])
print("list :",my_list)
print(type(my_list))
my_list[1] = 232323
print(my_list)
my_list = ['ravi',"monika",1722]
my_list12 = [23,44,4.4,43]
print(my_list)
print(len(my_list))
print(sum(my_list12))
print("")

#tuple
#immutable
#ordered/indexed
#repeated allowed
#accept all data-types
my_tuple = ((12,23.34,"monika"))
print("tuple :",my_tuple)
print(type(my_tuple))
print(my_tuple[1])
print("")

#dictionary
#mutable
#indexing not allowed
#unordered
#keys .... becuse keys are immutable , not repreated allolwed , not allowed datatrypes is :- list ,set,dict
#values ..... beacuse values are mutable , repeated allowed , allowed all data-types 
dictionary = {1:2,"rollno" : 23.32,"fruits":"banana",1:2}
print("dictionary : ",dictionary)
print(type(dictionary))
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary["fruits"])
dictionary["email"] = "ravi.octo12@gmail.com"
dictionary["rollno"] = "234343434"
print(dictionary)
print("")
#dict12 = {'banana','apple','banana','apple','banana','apple','pineaple','pineple'}
#print(dict12.count('apple'))

#set
#mutable
#indexing not allowed
#unordered
#doesnot allow duplicate members
#not alowed datatypes id :- set,dict,list
set1722 = {12,23.34,"monika"}
print("set :",set1722)
print(type(set1722))
print(len(set1722))
print("")
