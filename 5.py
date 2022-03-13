# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:11:10 2022

@author: user
"""
#Smallest Number
num1=float(input("Enter 1st number"))
num2=float(input("Enter 2nd number"))
num3=float(input("Enter 3rd number"))
if num1==num2==num3 :
    print("The numbers are equal")
elif num1<num2 and num1<num3 :
    print(num1," is the least")
    print(num2, " is the least")
else :
    print(num3, " is the least") 
