# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:27:03 2022

@author: user
"""

#Area & Perimetee of a Rectangle using Functions
def area(length, breadth):
    return length*breadth
    
def perimeter(length,breadth):
    return (length+breadth)*2
    
l=float(input("Enter length of the rectangle")) 
b=float(input("Enter breadth of the rectangle"))

print("The area is : ", round(area(l,b),2))     
print("The perimeteris : ", round(perimeter(l,b),2))

