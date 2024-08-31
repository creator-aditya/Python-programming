#Python is simple and easy
#Free and open source
#High level language
#Developed by Guido van Rossum
#Python is portable with different system like Mac and Window etc.

#First Program 
print("Hello World")

#Python Character Set
#Letters- A to Z, a to z
#Digits- 0 to 9
#Special Symbols => +,-,*,/ etc
#Whitespaces like Blank Space,Tab,carriage return,new line,formfeed
#Other Characters like Python can process all ASCII and Unicode characters as part of data

print("Aditya is my name.")
print("My age is 21.")

print("Aditya is my name.","My age is 21.")
print(23)
print(25+33)

#Variables is a name given to a memory location in a program
#Name is varable and Aditya is value
name = "Aditya" #String
age = 21        #Integer
price = 25.99   #Float

print(name)
print(age)
print(price)

print("My name is:",name)
print("My age is:",age)
print("Price is:",price)

age2 = age
print(age2)

#Rules for Identifiers
#Identifiers can be uppercase and lowercase, digit or an underscore(_)
#Example myVariable, variable_1, variable_for_print are all valid python idenrifiers
#An identifier cannot start with a digit like 1variable is not valid
#We cannot use special symbol like !,#,@,%,$ etc in our identifier
#Identifier can be of any length
#An identifier can also be defined as variable1 -This a valid identifier

print(type(name))
print(type(age))
print(type(price))

#Data Types in Python
#Integer like +ve value (12), -ve value (-23) and 0 (zero)
#String like name or any other alphabets , sentence or word,
#String can also be write in single quotes (''), double quotes ("") and tripple quotes (''' ''')
#Float values like decimal value eg. 23.99, 44.00
#Boolean values is either True or False
#Boolean values always write in capital values
#None data type represent no value 

age = 21
old = True
z = None

print(type(old))
print(type(age))
print(type(z))

#Reserved Keywords are the keywords that are reserved in python
#Python is a case sensitive language like small a and capital A both are different values

#Print sum of 2 number
m = 143
n = 928
sum= m+n
print(sum)

'''Comments in Python
Comments are part of program whcih does not execute in program
Comments are reprsented by Hash(#)
Single line comment is represented by (#) '''
#Multiline comments are represented by (''' '''')
''' This is a multiline comment '''
""'This is also a multline comment "'
#Shortcut for multiline comment is ctrl + / 

#Operators in Python
'''
Arithmetic Operators (+,-,*,%,**)
Relational/ Comparision Operstors(==,!=,>,<,>=,<=) 
Relational operator are used for comparision of values
Relational operator always provide boolean value either True or False

Assignment Operator are used to assign the values (=,+=,-=,*=,/=,%=,**=) - eg. a=23
Logical Operator works on Boolean value (not,and,or)
Logical Operator provides opposite return
'''

#Arithmetic Operator
q = 12
w = 34
print(q + w)
print(q - w)
print(q * w)
print(q ** w) #find power
print(q % w) #helps to find remainder value

#Relational Operator
l = 12
p = 21

print(l == p) #False
print(l != p) #True (Value of l is not equal to value of p)
print(l >= p)
print(l <= p)

#Assignment Operator
num = 10
num = num+12
num = num-1
num = num*2
num = num/2 #Divide
num = num%2 #Remainder value
num = num**5 #Find Power
print("num:",num)

#Logical Operator - not operator
# print(not False)
# print(not True)
c = 56
d = 23
print(not (c>d))
print(not (c<d))

#Logical Operator - And operator
value1 = True
value2 = True
print("ans operator:",value1 and value2) #If both the value are equal then the result is True and if both the value are not equal then the output is False

#Example of False 
value12= False
value11= True
print(value11 and value12)

#OR Operator
value1 = True
value2 = False
print(value1 or value2) #If one value is correct between value1 and value2

#Type Conversion in Python
#Float is superior than integer value
w = 23
x = 23.00
sum = (w+x)
print(sum) #23+23.00

#Type Casting
a = int("26")
b = 23.84
sum = (a+b)
print(sum)

#Conversion of Float to String
a = 255.98
print(type(str(a)))

#Input in Python
#Input() statement is used to accept the values from user
#The result for input statement is always a String type

name = input("enter your name:")
print("Your name is:",name)

#Conversion to Int type
number = int(input("enter your numb:"))
print("Your name is:",number)


#Practice Question
#Write a program to input 2 number and print their sum
first = int(input("Enter your number:"))
second = int(input("Enter your number:"))
sum = (first + second)
print(sum)


#Write a program to input side of a square and print it's area
side = float(input("Enter the side of square"))
area = (side**side)
print(area)

#Write a program to input 2 floating point number and print their average
a = float(input("Enter the value:"))
b = float(input("Enter the value:"))
average = (a+b)/2
print(average)

#Write a program to input 2 int number a and b , Print True if a is greater than or equal to b . If not print False
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print(a>=b)
