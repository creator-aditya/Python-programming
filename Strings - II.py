#Strings and Conditional Statements

#Esacpe sequence character (tab(\t),new line(\n) etc)

str1 = "This is a string.\nwe are creating it in python"
print(str1)

#Strings is a data types that stores a sequence of characters
#Basic Operations
#Concatenation=> "Hello" + "World" => "HelloWorld"
#Concatenation is the process of adding the words

str1 = "Hello"
str2 = "world"
print(str1+str2)

#Length Function - It is used to find the length of string
#It also includes empty spaces in length.
str1 = "Test user"
print(len(str1))


#Indexing is alloting a position to the character when a string is created
#We cannot change the character in indexing

str1 = "This is a new string"
print(str1[5])

#Slicing - Accessing the part of a string
#Ending index is not included in slicing

str1 = "Hello everyone it's me"
print(str1[2:4]) #The result will be llo because ll and o is not included in this. 


#Negative Index in Slicing
fruit = "Apple"
print(fruit[-3:-1]) #The result for this is pl (-1 e from apple is not included)

'''String Functions
string.endswith("value") #Return true if string ends with value
string.capitalize() #Capitalize first character
string.replace("old","new") #It replaces all the old values to new values
string.find("word") #Return first index of 1st occurence 
string.count("word") #Count all the occurence of substring
'''

str1 = "This is a python code"
print(str1.endswith("code")) #Endswith function - return true if the the string ends with code

str1 = "this is a fruit"
print(str1.capitalize()) #It capitalize the first character of the str1 and the output will be "This is a fruit"

str3 = "I'm studying python"
print(str3.replace("I'm","We are")) #Replace function replaces the I'm with with are and the output is We are studying python

str1 = "This is my personal number"
print(str1.find("m")) #Return first index of 1st occurence 

str1 = "Hello to everyone here,Hello to myself"
print(str1.count("Hello")) #Count function count all the occurence from the string - Hello is repeat 2 time in the string so the output is 2 count


#Practise Question
#Write a program to input user first name and print it's length
name = str(input("Enter your name"))
print(len(name))

#Write a program to find the occurence of '$' in a string
str = "Price of $ is 80 but sometime the price of $ is 81"
print(str.count("$"))









