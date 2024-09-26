#A variable is essentially a container used to store data. 
#It can be used to store different types of data.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
#The variable name must start with a letter or an underscore (_), and cannot contain spaces.
#tpyes of variables
#1. Global Variable
#2. Local Variable
#3. Instance Variable
#4. Class Variable
#Data types in python
#1. int
#store integer values
a = 10
print(a)
#2. float
#store floating point values
b = 0.7
print(b)
#string
#store string values
c = "hello"
print(c)
#boolean
#Represents True or False values.
d = True
print(d)
#this are all primitive data types in python which are immutable or unchangeable

#moving on to complex data types which are mutable or changeable
#1. List : A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
e = [1,2,4,5]
# item can be accessed in a list using index
print(e[0])
#2. Tuple : A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
f = (1,2,3,4)
# some operations can be performed on tuple inclde 
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
print(f.count(1)) #output 1 because 1 is present only once in the tuple
#dictionary : A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
g = {
    "name" : "jude",
    "age" : 23
}
#item can be accessed in a dictionary using key
print(g["name"])
#set : A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
h = {1,2,3,4,5}
#item can be accessed in a set using loop   
for i in h:
    print(i) #output 1,2,3,4,5 because set is unordered and unindexed and it does not allow duplicate values and it is mutable and changeable
#python naming convention
#1. Variable names are case-sensitive
#2. Variable names must start with a letter or an underscore
#3. Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#4. Variable names cannot start with a number
#5. Variable names should be descriptive and meaningful
#6. Avoid using special characters in variable names
#7. Avoid using reserved keywords as variable names
#8. Use camelCase notation for naming variables
#9. Use underscore notation for naming variables
#10. Use capital letters for naming constants
#11. Use lowercase letters for naming functions and methods
#12. Use capital letters for naming classes
#13. Use a leading underscore for naming private variables
#some built in variable functions in python
#1. type() : returns the type of the variable
print(type(a))
#2. id() : returns the memory address of the variable
print(id(a))
#3. len() : returns the length of the variable
print(len(a))
#4. del() : deletes the variable
del(a)
