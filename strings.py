# -*- coding: utf-8 -*-
"""
How to Declare Strings?
"""

#Using Single Quotes

a = 'Python'

#print(a)

#Using Double Quotes

b = "Python for Beginners"

#print(b)

#Using Triple Quotes to Span across a Line

c = '''Hello
World
!
'''

#print(c)

#Using \n, \t, \\ - Escape sequences

#d =  "Hello\tWorld\t!"
#
#print(d)

#Using single and Double quotes

#str = 'Python "for" Beginners' 
#
#print(str)
















"""
How to Access Strings
"""

##Forward Indexing

#str = "Hello"
##
#print(str[0])
#print(str[1])
##
#print(len(str))
##
#a= "Python is awesome!"
#print(len(a))
#print(a[17])
#for():
#    print(str[i])


##Backward Indexing

#str = "Hello" 
##
#print(str[-1])
#print(len(str))
#print(str[-2])
#print(str[-5])
#
#print(str.len())
#
#for():
#    print(str[i])
















"""
String Slicing
"""

#st = "Cats are cute and lovely."
#sub = st[-16:-12]
##print(len(st))
##Cats are cute
##-25, -24, -23, -22, -21
##
#print(sub)


















"""
String Concactenation
"""

#x = "Python and "
#y = 'Java'
#
#+
#print(x + y)
#
#*
#print((x+y)*3)
#
#print(y + 10)
#
#print(y + '10')
#print(x + '3.14')
















"""
String Formatters
"""

###Using Commas

#occ = "Coding"
##
#print("I am good at",occ)
#print(f"I am good at {occ}")


##Using the f-method

#name = 'Divya'
#print(f'My name is {name}')

















"""
String Formatters
"""

##Using the format method

#quantity = 3
#itemno = 567
#price = 49.95
#myorder = "I want {0} pieces of item {1} for {2} dollars."
#print(myorder.format(quantity, itemno, price))
#
#quantity = 3
#itemno = 567
#price = 49.95
#myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
#print(myorder.format(quantity, itemno, price))
#
#print("I want {num} {fruit}".format(num=5, fruit="mangoes"))



###Using the % operator

name = "Sita"
age = 22
money = 15.55
print ("%s's age is %d. She has %f dollars with her"%(name,age, money))

