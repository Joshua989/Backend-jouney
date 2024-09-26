#loops are used to iterate over a sequence of elements
#in simple terms, loops are used to repeat a block of code multiple times
#while loop : this is a kind of loop that runs as long as a condition is true
#syntax: while condition:
#            #code block
#            #code block
#            #code block
# #example of while loop
x = 3
while x < 10:
    print(x)
    x += 1 #output 3 4 5 6 7 8 9
    # a more complex example of while loop
    #create a function that takes a list of numbers and returns the sum of the numbers
def sum(numbers):
    total = 0 #initialize a variable to store the sum of the numbers
    index = 0 #initialize a variable to store the index of the numbers
    while index < len(numbers):#check if the index is less than the length of the numbers
        total += numbers[index]#add the number at the index to the total in simple terms, total = total + numbers[index]
        index += 1
    return total
#function call
x = sum([1,2,3,4,5])
print(x) #output 15
#usimg and in while loop
x = 1
while x < 3 and x == 4:
    print(x)
    x += 1 #output 1

#for loop : this is a kind of loop that runs for a specific number of times
#syntax: for item in sequence:
#            #code block
#            #code block
#            #code block
# #example of for loop 
for x in range(5): #output 0 1 2 3 4
    print(x)
# #example of for loop with a list
names = ["ade", "john", "mary"]
for name in names:
    print(name) #output ade john mary
# looping through a dictionary
# create a dictionary
mydict = {
    "one": 1,
    "two": 2,
    "three": 3
}
#loop through the dictionary
for key in mydict:
    print(key) #output one two three
#brake statement in loops is used to stop the execution of the loop based on a condition
x = [1,2,3,4,5]
for item in x:
    if item == 3:
        break
    print(item)

 #nested loops : this is a kind of loop that is inside another loop mostly used 
 # to iterate over a sequence of elements
 # in web development, nested loops are used to iterate over a list of items in a list   
    # syntax: for item in sequence:
    #             for item in sequence:
    #                 #code block
    #                 #code block
    #                 #code block
    # #example of nested loop
    # #create a list of fruits
    frruit = ["apple", "banana", "cherry"]
    #create a list of colors
    colors = ["red", "yellow", "pink"]
    #loop through the fruits
    for food in frruit:
        #loop through the colors
        for color in colors:
            print(food, color) #output apple red apple yellow apple pink banana red banana yellow banana pink cherry red cherry yellow cherry pink
#2d list in python
my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(my_list) #output [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#loop through the 2d list
for row in my_list:
    for item in row:
        print(item) #output 1 2 3 4 5 6 7 8 9

        #for commenting more than one line use 3 quatation mark
        '''
        vdhjbckd dcb jdkbldhbkdl jbcKC ckjbjdkC 
        cbdjkcd dshbcjKc nklnckd dcndklc 
        dcbdjcb dcbkcl
        '''