#python is an object oriented programming language
#objects are instances of classes i simple terms, objects are variables of classes
#classes are blueprints for creating objects in simple words, classes are used to create objects
#syntax: class ClassName:
#            #code block
#            #code block
#            #code block
# #example of a class
from new import inherit
class person:
    x = "ade"

person1 = person()
print(person1.x) #output ade


#init function in python it allows us to initialize the object with some values in simple terms, it is used to assign values to object properties
#syntax: def __init__(self, parameter):
#            self.parameter = parameter
# #example of init function
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = person("ade", 20)
print(student.name) #output ade
print(student.age) #output 20       

#getting input from users
# # #example of getting input from users
name = input("Enter your name: ")
age = input("Enter your age: ")
student2 =  person(name, age)
print(student2.name) #output ade
print(student2.age) #output 20
del student2.age#delete the age property
print(student2.age) #output error because the age property has been deleted

#pass statement in python
#the pass statement is used as a placeholder for future code
#syntax: pass
# #example
class person(inherit):#inheritance from the inherit class named new.py 
    pass

p1 = person()
print(p1.name)

