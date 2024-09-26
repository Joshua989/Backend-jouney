#dictionary are key value pairs that stores date in python
#they are changable and unordered and does not allow duplicate keys
#syntax: dictionary = {key1: value1, key2: value2, key3: value3}

my_dict = {
    "name": "ade",
    "age": 20,
    "is_student": True,
    "nationality": "nigeria"
}
print(my_dict)
#print only the value of a key
print(my_dict["name"]) #output ade
#change the value of a key
my_dict["name"] = "john" #output john
#you cant have two keys with the same name
#you can have a key with a different data type
#to get the length of a dictionary
print(len(my_dict)) #output 4
#mixing data types in a dictionary
mixed_dict = {
    "name": "ade",
    "age": 20,
    "is_student": True,
    "nationality": "nigeria",
    "hobbies": ["reading", "coding", "playing games"]
}
print(mixed_dict["is_student"]) #output True
x = mixed_dict["hobbies"]
print(x) #output ['reading', 'coding', 'playing games']