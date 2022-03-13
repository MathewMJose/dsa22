# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:49:11 2022

@author: user
"""
#Fibonacci Series
first_num=0
second_num=1
end_num=int(input("Enter the end number"))
if end_num<=0:
    print("Enter a positive integer")
else :
    while (first_num <=end_num):
        print(first_num)
        prev_num=first_num
        first_num=second_num
        second_num=prev_num+first_num
        
        
        
    

