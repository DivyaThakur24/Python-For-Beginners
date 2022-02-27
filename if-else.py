# -*- coding: utf-8 -*-
#if Statement
#Check if b is greater than a
#a = 133
#b = 100
#if(b<a):
#    print("b is less than a")


#if-else Statement
#Check if the number is odd or even
#n = int(input("Enter a number: "))
#if (n%2==0):
#    print(n,"is an even number.")
#else:
#    print(n,"is an odd number.")
    
    
#if-else statements using logical operators
#Check if the number is divisible by 5 or 3
#n = int(input("Enter a number: "))
#if(n%5==0):
#    print(n, "is divisible by 5")
#elif(n%3==0) :
#    print(n, "is divisible by 3")
#else:
#    print(n, "is divisible neither by 5 nor by 3")
  







  
#if-else statements using nested if-else
#Check if the number is divisible by 15 or 10 or by both
#15 = 5 * 3
# 10 = 5 * 2
#n = int(input("Enter a number: "))
#if(n%5==0):
#    if(n%3==0 and n%2==0):
#        print(n, "is divisible by both 15 and 10")
#    elif(n%3==0):
#        print(n, "is divisible by 15 only")
#    elif(n%2==0):
#        print(n, "is divisible by 10 only")
#    
#else :
#    print(n, "is neither divisible by 15 nor by 10")



#if else statements using logical operator 
#Check if the number is divisible by both 5 
#and 3 or check if it's divisible by 7 or 3
n = int(input("Enter a number: "))
if(n%5==0 and n%3==0):
    print(n, "is divisible by 15")
elif(n%7==0 or n%3==0):
    print(n, "is divisible by 7 or by 3 or by both")
    
