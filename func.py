# -*- coding: utf-8 -*-

#Declare a function
def greet():
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + "Divya" + ". Good morning!")
    
#Call a function
#greet()

#Print docstring
#print(greet.__doc__)
#
##Functions containing return values
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num
# 5 = 5, 0 = 0, -5 = -(-5) = 5
#
print(absolute_value(2))
#
print(absolute_value(-4))
#
##Scope and lifetime of variables of a function
def my_func():
	x = 10
	print("Value inside function:",x)
#
x = 20
my_func()
print("Value outside function:",x)
#
##Default Arguments
#def greet(name, msg="Good morning!"):
#    """
#    This function greets to
#    the person with the
#    provided message.
#
#    If the message is not provided,
#    it defaults to "Good
#    morning!"
#    """
#
#    print("Hello", name + ', ' + msg)
#
#
#greet("Kate")
#greet("Bruce", "How do you do?")
#
##def greet(msg="Good morning!", name):
##    """
##    This function greets to
##    the person with the
##    provided message.
##
##    If the message is not provided,
##    it defaults to "Good
##    morning!"
##    """
##
##    print("Hello", name + ', ' + msg)
##
##greet("Kate")
#
##Arbitrary Arguments
##Sometimes, we do not know in advance the number of arguments that will be passed into a function. 
##Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.
##In the function definition, we use an asterisk (*) before the parameter name to denote this kind of argument.
#
#def greet(*names):
#    """This function greets all
#    the person in the names tuple."""
#
#    # names is a tuple with arguments
#    for name in names:
#        print("Hello", name)
#
#
#greet("Monica", "Luke", "Steve", "John")
#
##Import Modules
#import example
#
#x = example.add(4.5, 5)
#print(x)
#
## import statement example
## to import standard module math
#
#import math
#print("The value of pi is", math.pi)
#
## import module by renaming it
#import math as m
#print("The value of pi is", m.pi)
#
## import only pi from math module
#from math import pi
#print("The value of pi is", pi)



