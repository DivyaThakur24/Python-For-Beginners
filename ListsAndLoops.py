# -*- coding: utf-8 -*-

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
thislist = [1, 3, True, "abc"]
#print(thislist)
#homogeneous items in a list are preferred

#Access List items using forward and backward indexing
print(fruits[1])
print(fruits[-1])
#
##Return a range of indices
print(fruits[-4:-1])
print(fruits[1:5])
#
##Check if apple is present in the list of fruits
if("apple" in fruits) :
  print("Yes, 'apple' is in the fruits list")

#Change list items
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[1:2] = ["blackcurrant", "watermelon"]
print(fruits)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[1:3] = "watermelon"
print(fruits)

#To insert a new list item, without replacing any of the existing values, 
#we can use the insert() method.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.insert(2, "watermelon")
print(fruits)

#Looping
for i in range(len(fruits)):
  print(fruits[i])
  
i=0
while i<len(fruits):
    print(fruits[i])
    i = i+1
    
#Based on a list of fruits, you want a new list, 
#containing only the fruits with the letter "a" in the name.
newlist = list()
#
for x in fruits:
  if "a" in x:
   newlist.append(x)
#
print(newlist)

#With list comprehension you can do all that 
#with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
#
print(newlist)   

  