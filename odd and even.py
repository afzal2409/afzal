# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 00:28:33 2021

@author: exam
"""

n=int(input("enter value for n:"))
ep=0
op=0
for i in range(1,n+1):
    if i%2==0:
        ep+=i
    else:
        op+=i
print("sum of even places:",ep)
print("sum of odd places:",op)