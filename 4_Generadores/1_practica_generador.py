#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:14:58 2020

@author: danielbarraza
"""
"""
GENERADORES

    * Son Estructuras que extraen valores de una función y se almacenan en objetos iterables QUE SE PUEDEN RECORRER.
    
    * Estos valores se almacenan de uno en uno.
    
    * Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente.
      Esta característica es conocida como "Suspención de estado".
    
"""

def generaPares(limite):
    num=1
    miLista=[]
    
    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))

#=============================================================================

def generaPares(limite):
    num=1
    
    while num<limite:
        
        yield num*2
        
        num=num+1
    
devuelvePares=generaPares(10)

for i in devuelvePares:
    
    print(i)
    
#=============================================================================

def generaPares(limite):
    num=1
    
    while num<limite:
        
        yield num*2
        
        num=num+1
    
devuelvePares=generaPares(10)

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

