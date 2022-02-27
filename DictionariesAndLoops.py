# -*- coding: utf-8 -*-

#Create a dictionary
dict1 = {"a":1, "b":2, "c":3}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(type(thisdict))

#Duplicates not allowed
#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#  "year": 2020
#}

#print(thisdict)

#Access Keys, values, items, single value
x = thisdict.keys()
print(x)
y = thisdict.values()
print(y)
z = thisdict["model"]
print(z)
z = thisdict.get("model")
print(z)
#
a = thisdict.items()
print(a)

#Change items
thisdict["year"] = 2018
print(thisdict)
#
thisdict.update({"year" : 2020})
print(thisdict)
#
##Add items
thisdict["color"] = "red"
print(thisdict)
#
thisdict.update({"engine" : "4951cc"})
print(thisdict)
#
##Remove items
thisdict.pop("engine")
print(thisdict)
del thisdict["color"]
print(thisdict)
#
##Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
#  
##Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
#  
##You can also use the values() method 
##to return values of a dictionary:
for x in thisdict.values():
  print(x)
#  
##You can use the keys() method 
##to return the keys of a dictionary:  
for x in thisdict.keys():
  print(x)
#  
##Loop through both keys and values, 
##by using the items() method:
for x, y in thisdict.items():
  print(x, y)



