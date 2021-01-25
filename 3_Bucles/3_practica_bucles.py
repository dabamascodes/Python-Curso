#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:43:48 2020

@author: danielbarraza
"""

for letra in "Python":
    print("Viendo la letra: " + letra)
    
for letra in "Python":
    
    if letra=="h":
        continue
    
    print("Viendo la letra: " + letra)

#=============================================================================

nombre="Pildoras Informáticas"


contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1
     
print(contador)

#=============================================================================

while True:
    pass

class MiClase:
    pass # Para implementar más tarde

#=============================================================================

email=input("Introduce tu email, por favor: ")

    
for i in email:
    
    if i=="@":
                
        arroba=True
        
        break;

else:
    
    arroba=False    

print(arroba)

