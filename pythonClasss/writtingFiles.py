#writting files in python
#this is used to write to a file in python
#syntax: open the file
#        write to the file
#        close the file
#open the file
open_file = open("list.py", "w")#the w means write we also have r for read, a for append, x for create etc r+ for read and write    
#write to the file
open_file.write("this is a new line")#this will write to the file overwriting the existing content
#close the file
open_file.close()
#to append something to the buttom
open_file = open("list.py", "a")#the a means append we also have r for read, w for write, x for create etc r+ for read and write
open_file.write("this is a new line")#this will write to the file appending to the existing content
open_file.write("\nthis is a new line")# this will write to the file appending to the existing content in a new line
open_file.close()
#to craete a new file
open_file = open("list.py", "x")#the x means create we also have r for read, w for write, a for append etc r+ for read and write
open_file.write("this is a new line")#this will write to the file creating a new file
open_file.close()