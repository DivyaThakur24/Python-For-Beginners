# -*- coding: utf-8 -*-
#Homogeneous
set1 = {1,2,3,4,5}
set2 = {True, False, False}
print(set1)
print(set2)
print(type(set1))
#Heterogeneous
set3 = {"abc", 34, False, 240, "female", "abc"}
#
#print(set1)
#print(set2)
print(set3)
print(type(set3))

#Add an item to a set
set3.add("FirstName")
print(set3)

#Add another set or even a list to a set
set1.update(set2)
print(set1)
print(set2)

#Remove items from a set
set3.remove("FirstName")
print(set3)

#If the item to remove does not exist, remove() 
#will raise an error.
#set3.remove("LastName")
#If the item to remove does not exist, discard() 
#will not raise an error.
set3.discard("LastName")

#Loop through Sets
thisset = {"apple", "banana", "cherry"}
#
for x in thisset:
  print(x)
#  
i=0
while (i<len(thisset)):
    print(thisset[i])
    i = i+1
