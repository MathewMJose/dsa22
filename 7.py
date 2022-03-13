# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:49:11 2022

@author: user
"""
#Hour to seconds
def to_seconds(t):
    sec=t*60*60
    return sec

hours=int(input("Enter the no. of hours"))

print(hours, " Hours is equal to : ", to_seconds(hours), " seconds")
