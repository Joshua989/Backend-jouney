'''
try except block is used to handle exceptions in python
in simple terms, it is used to handle errors in python
'''
#syntax: try:
#            #code block
#            #code block
#            #code block
#        except:
#            #code block
#            #code block
#            #code block
# #example of try except block
try:
    x = int(input("Enter a number: "))
    print(x)
except:
    print("something went wrong")

#validate the input
# #example of try except block
try:
    x = int(input("Enter a number: "))
    print(x)
except ValueError:
    print("please enter a number")  
else:
    print("you entered a number")      
#fianlly block it runs no matter what
finally:
    print("the code has ended")