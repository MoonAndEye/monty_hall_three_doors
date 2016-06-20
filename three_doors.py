# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:10:35 2016

"""
import random as rd

doors = [0,0,0]



def changeDoor(doors=list):
    #allChoice = [0,1,2]
    car = rd.randint(0,len(doors) - 1)
    doors[car] = 1
    playerchoice = rd.randint(0,len(doors) - 1)
    if doors[playerchoice] == 1:
        return(0)
    else:
        return(1)

result = []
flag = 0
while flag < 1000:
    doors = [0,0,0]
    a = changeDoor(doors)
    result.append(a)
    flag = flag + 1
print(result)
