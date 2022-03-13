# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:27:38 2022

@author: user
"""
rows=int(input("Enter the no. of rows"))
for i in range(rows+1): 
    for j in range (rows-i):
        print(" ", end="")
    for p in range(i):
        print("* ",end="")
    print("\n")            

    