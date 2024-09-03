#Conditional Statements
#if-elif-else

age = 11
if(age >= 18):
    print("Eligible")
elif(age <= 17):
    print("Not Eligible")


#elif Statement
light = "Green"

if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Wait")
elif(light == "Green"):
    print("Go")

#if-else statement
number = 18
if(number >= 18):
    print("Number is valid")
else:
    print("Number not valid")

#Grade of students based on marks
marks = int(input("Enter the marks"))
if(marks >= 90):
    print("A")
elif(marks >=80 and marks <90):
    print("B")
elif(marks >=70 and marks < 80):
    print("C")
elif(marks >=60 and marks <70):
    print("D")
else:
    print("FAIL")


#Nesting
value = int(input("Enter the value"))

if(value >= 18):
    if(value>=80):
        print("Cannot Drive")
    print("Can Drive")
else:
    print("Cannot Drive")


#Practice
#Write a program if a number entered by the user is odd or even
number = int(input("Enter your number: "))
if(number % 2 == 0):
    print("Even")
else:
    print("Odd")


#Write a program to find the greatest of 3 numbers entered by the user
value1 = int(input("Enter number one: "))
value2 = int(input("Enter number two: "))
value3 = int(input("Enter number three: "))
if(value1>value2 and value1>value3):
    print("Value 1 is greater than other")
elif(value2>value3):
    print("Value 2 is greater than other")
else:
    print("Value 3 is greater than other")

#Write a program to check if a number is a multiple of 7 or not
number = int(input("Enter your number: "))
if(number % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")