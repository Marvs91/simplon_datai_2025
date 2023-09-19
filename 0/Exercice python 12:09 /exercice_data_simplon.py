#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:03:14 2023

@author: marvs
"""

#EXERCICE 1

nombre = input("nombre positif")
for i in range(int(nombre)):
    print(i+1)
    
#EXERCICE 2   

def positif(nombre):
    a=[]
    for i in nombre:
        if i>0:
            a.append(i)
    return a 

nombre =[-3,-2,-1,0,1,2,3,4]
print(positif(nombre))

#EXERCICE 3

def voyelle(liste):
    a=[]
    for i in liste:
        if i 