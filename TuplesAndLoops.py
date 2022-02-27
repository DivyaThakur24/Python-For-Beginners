# -*- coding: utf-8 -*-

#Create Tuples
#Heterogeneous
tuple1 = ("abc", 34, True, 40, "male")
#Homogeneous
tuple2 = ("a", "b", "c", "d")

print(tuple1)
print(tuple2)
print(type(tuple1))

#Access Tuples
print(tuple1[-2])
print(tuple2[1:3])

#Updating a Tuple
#Once a tuple is created, you cannot change its values. 
#Tuples are unchangeable, or immutable as it also is called.

y = "kiwi"
x = list(tuple1)
x.append(y)
tuple1 = tuple(x)
print(tuple1)

#You cannot remove items from a tuple
z = list(tuple1)
z.remove("kiwi")
tuple1 = tuple(z)
print(tuple1)

#Unpacking a tuple
#Extracting the values back into variables
fruits = ("apple", "banana", "cherry")
#
(green, yellow, red) = fruits
#
print(green)
print(yellow)
print(red)

#Using Asterisk*
#If the number of variables is less than the number of values, 
#you can add an * to the variable name and 
#the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
(green, yellow, *red) = fruits
#
print(green)
print(yellow)
print(red)

#Can add to any variable, even in the middle
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
(green, *tropic, red) = fruits
#
print(green)
print(tropic)
print(red)

#Looping through tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#  
print(len(thistuple))
#range(3) _> 0,1,2
for i in range(len(thistuple)):
  print(thistuple[i])
#  
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



