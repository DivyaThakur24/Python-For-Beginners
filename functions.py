# -*- coding: utf-8 -*-

#Define a function
#def my_function():
#  print("Hello from a function")
  
#Calling a function
#my_function()

#A function that takes two parameters
def my_function(fname, lname):
  print(fname + " " + lname)

#my_function("Divya", "Thakur")

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[0])
#
my_function("Emil", "Tobias", "Linus")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

#my_function("Sweden")
my_function("India")
#my_function()

