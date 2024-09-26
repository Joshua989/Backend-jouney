#tuples are collection of items which is ordered and unchangeable
#syntax: tuple = (item1, item2, item3)
#tuples are immutable
three_numbers = (1,2,3)
#getting the length of the tuple
print(len(three_numbers))
#getting an item from the tuple
print(three_numbers[0])
#getting thetype of the tuple
print(type(three_numbers))
strings = ("home", "school", "church")
#it allow various data types
# you can also have a combination of datatypes
mixed = (1, "home", True)
print(mixed)
#checking the type of a perticauler item in the tuple
print(type(mixed[0]))
#tuple contructor are  used to create a tuple in python
#syntax: tuple = tuple((item1, item2, item3))
contructor = tuple(("home", "school", "church"))