# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:58:11 2022

@author: user
"""
#Favourite Foods
food=[]
count=5
print("\n What are your 5 favourite foods \n")
for i in range(count):
    item=str(input())
    food.append(item)
for i in range(count):
    print("I like ", food[i])
    