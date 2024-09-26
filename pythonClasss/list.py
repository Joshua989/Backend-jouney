#you would be working with a lot of data in backend development
#and you would need a list
#a list is a collection of items that are ordered and changeable
#syntax of a list
#list_name = [item1, item2, item3]
# #example of a list
numbers = [1,2,3,4,5]
#each list item has an index
#the index starts from 0
print(numbers[0]) #output 1
print(numbers[1]) #output 2
print(numbers[2]) #output 3
print(numbers[3]) #output 4
print(numbers[4]) #output 5
countris = ["nigeria", "ghana", "usa", "uk"]
print(countris[0]) #output nigeria
print(countris[1][4]) #output a
#get from index 1 to 3
print(countris[1:3]) #output ['ghana', 'usa']
#specifying range of index
print(countris[2:3]) #output ['usa']
#geting the type of a list
print(type(countris)) #output <class 'list'>
#cahnging the value of a list
countris[0] = "canada"
print(countris) #output ['canada', 'ghana', 'usa', 'uk']
#looping through a list this is used to access all the items in a list nad perform some operation on them
for country in countris:
    print(country)
#check if an
if "canada" in countris:
    print("canada is in the list")
#check the length of a list
print(len(countris)) #output 4
##using negative index
#negative index starts from the end of the list
print(countris[-1]) #output uk