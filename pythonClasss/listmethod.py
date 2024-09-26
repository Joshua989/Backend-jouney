#list methods
list = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list.extend(list2)
print(list) #output [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'] #extend() adds the elements of a list to another list
list.append(6) #append() adds an element to the end of a list
print(list) #output [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', 6]
print(len(list2)) #output 5 #len() returns the length of a list
#puttin a number beteeen 3 qnd 4
list.insert(3,3.5) #insert() adds an element at a specified index
#to remove an element from a list
list.remove(3) #remove() removes the first occurence of an element from a list
#clearing the list
list.clear() #clear() removes all the elements from a list
#getting index of an element
print(list2.index("c")) #output 2 #index() returns the index of the first occurence of an element
#counting the number of occurence of an element
print(list2.count("c")) #output 1 #count() returns the number of occurence of an element
#reversing the list
list2.reverse() #reverse() reverses the order of elements in a list
list.sort() #sort() sorts the elements of a list very usefulo wen working in python
#duplicating a list
list3 = list2.copy() #copy() returns a copy of a list
#pop removes the last element of a list
list2.pop() #pop() removes the last element of a list
