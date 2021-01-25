#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:44:56 2020

@author: danielbarraza
"""

def mensaje():
    print ("Estamos aprendiendo Python")
    print ("Estamos aprendiendo instrucciones básicas")
    print ("Poco a poco iremos avanzando")
    
def suma():
    num1=5
    num2=7
    print(num1+num2)
    

def suma1(num1,num2):
    print(num1+num2)   
    
def suma2(num1,num2):
    res=num1+num2
    return res
    
mensaje()

suma()

suma1(6,7)

suma1(7,8)

ans=suma2(1,1)

print(ans)



