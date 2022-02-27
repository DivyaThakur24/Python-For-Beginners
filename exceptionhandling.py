# -*- coding: utf-8 -*-

#print(x)

#The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occurred")
  
#Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except SyntaxError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
    
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
  
##As a Python developer you can choose to throw an exception if a condition occurs.
    
#Raise an error and stop the program if x is lower than 0:
#x = -1
#
#if x < 0:
#    raise Exception("Sorry, no numbers below zero")

#Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")

