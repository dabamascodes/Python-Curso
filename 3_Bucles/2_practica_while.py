#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:01:11 2020

@author: danielbarraza
"""


i=1

while i<=10:
    print("Ejecución " + str(i))
    i=i+1
    
print("Terminó la ejecución")

#=============================================================================

edad=int(input("Introduce tu edad por favor: "))

while edad<0:
    print("Has introducido una edad negativa. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))
    
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))

#=============================================================================

edad=int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
    print("Has introducido una edad negativa. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))
    
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))

#=============================================================================
import math
print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raíz de un número negativo")
    
    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;
    
    numero=int(input("Introduce un número por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))