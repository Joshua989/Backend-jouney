#if statement are used to check if a condition is true or false
#it allows python to make decision based on the result of the condition
#syntax: if condition:
#            #code block
#            #code block
#            #code block
# #example of if statement
# #create a function that checks if a number is greater than 10
number = int(input("Enter a number: "))
if number > 10:
    print("number is greater than 10")
# #output number is greater than 10
if number < 10:
    print("number is less than 10")
# #output number is less than 10
if number == 10:
    print("number is equal to 10")
# #output number is equal to 10
if number == True:
    print("number is true")
# #output number is true
if number == False:
    print("number is false")
if number != 10:
    print("number is not equal to 10")
 #output number is not equal to 10
 #        if else statement
    #        the if else statement is used to check if a condition is true or false if the if statement is not true
    #        the else statement is executed
    #        syntax: if condition:
    #                    #code block
    #                    #code block
    #                    #code block
    #                else:
    #                    #code block
    #                    #code block
    #                    #code block
    # #example of if else statement
    a = 10
    b = 20
    if a > b:
        print("a is greater than b")
    elif a == b:
            print("a is equal to b") #output a is equal to b it is used to check if the first condition is not true
    else:
        print("a is less than b")

        # using or and and in if statement
        # the or keyword is used to combine two or more conditions
        # the or keyword is used to check if any of the conditions is true
        # syntax: if condition1 or condition2:
        #             #code block
        #             #code block
        #             #code block
        # #example of or keyword
        # #create a function that checks if a number is greater than 10 or less than 5
        def number_checker(number):
            if number > 10 or number < 5:
                print("number is greater than 10 or less than 5")
            elif number == 5 or number == 10:
                print("number is equal to 5 or 10")
            else:
                print("number is between 5 and 10")
        #function call
        number_checker(3) #output number is greater than 10 or less than 5
        