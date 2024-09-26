'''
reading file
this is used to read a file in python
examples of files are text files, csv files, excel files, pdf files etc

'''
#the syntax for reading a file in python
#open the file
#read the file
#close the file
open_file = open("list.py", "r")#the r means read we also have w for write, a for append, x for create etc r+ for read and write
print(open_file.read()) 
open_file.close() #this is used to close the file
print(open_file.readline()) #this is used to read the first line of the file
print(open_file.readlines()) #this is used to read all the lines of the file
#loop through the file
for line in open_file:
    print(line)