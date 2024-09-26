#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
#syntax of a function
# def function_name(parameters):
#     #code block
#     return value
# #function call
# function_name(arguments)
# #example of a function 
#create a function that takes two arguments and returns their sum
def sum (a,b):
    return a+b
#function call
print(sum(2,3)) #output 5

# #function with default parameter
# #create a function that takes two arguments and returns their sum
def sum (a=0,b=0):
    return a+b
#function call
print(sum()) #output 0
#some othe more examples of functions
# #create a function that takes a string as an argument and returns the length of the string
def name_lenntgh(name):
    return len(name)
#function call
length = name_lenntgh("ade")
print(length) #output 3
# #create a function that takes a string as an argument and returns the string in uppercase
def uppercase(name):
    return name.upper()
#function call
upper = uppercase("ade") 
print(upper) #output ADE
# some more complex example related to backend development
# #create a function that takes a list of numbers and returns the sum of the numbers
def sum (numbers):
    total = 0
    for number in numbers:
        total += number
    return total
#function call
print(sum([1,2,3,4,5])) #output 15
#example related to string manipulation
# craete a function that greate a greeting messageto a person
def greetings(name):
    return "hello" + name
#function call
print(greetings("ade")) #output hello ade
#function annotation in python
#function annotation is a way to add metadata to a function parameters and return value
#in simple terms, it is a way to specify the data type of the function parameters and return value
#syntax of function annotation
# def function_name(parameter: data_type) -> return_data_type:
#     #code block
#     return value
# #example of function annotation
def greet(name: str) -> str:
    return "hello" + name
#function call
print(greet("ade")) #output hello ade
# #function with multiple return values
# #create a function that takes two numbers and returns their sum and product
def sum_product(a,b):
    return a+b, a*b
#function call
result = sum_product(2,3)
print(result) #output (5,6)
#recursive function
#A recursive function is a function that calls itself during its execution
#in simple terms, a function that calls itself is called a recursive function
#for example, the factorial of a number is calculated using a recursive function
#factorial of a number is the product of all positive integers less than or equal to that number
#factorial of 5 is 5*4*3*2*1 = 120
#syntax of a recursive function
# def function_name(parameters):
#     if base_condition:
#         return base_value
#     else:
#         return function_name(modified_parameters)
# #example of a recursive function
# #create a function that calculates the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)
#function call
print(factorial(5)) #output 120
#lambda function
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#syntax of a lambda function
# lambda arguments : expression
# #example of a lambda function
# #create a lambda function that takes two arguments and returns their sum
sum = lambda a,b : a+b
#function call
print(sum(2,3)) #output 5
def greeting (*names):#passing multiple arguments
    print("welcome" + names[2])

    greeting("ade", "ola", "bola")#output welcome bola
name_boy = input("enter your name")
def name(name_boy):
    print("hello", name_boy)

name(name_boy)