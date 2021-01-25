#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:06:24 2020

@author: danielbarraza
"""

"""
Estructura de datos que nos permite almacenar gran cantidad de valores
(equivalente a los array en otros lenguajes de programación)

En Python las listas pueden guardar diferente tipo de valores 
(en otros lenguajes no ocurre esto con los array)

Se pueden expandir dinámicamente añadiendo nuevos elementos
(otra novedad respecto a los arrays en otros lenguajes)
"""

miLista=["María","Pepe","Marta","Antonio"]

print(miLista[:])

print(miLista[0])

print(miLista[-2])

#Poción de lista
print(miLista[0:3])

print(miLista[:3])

print(miLista[1:4])

print(miLista[2:])

miLista.append("Daniel")

print(miLista[:])

miLista.extend(["Sandra","Daniel","Lucía"])

print(miLista[:])

print(miLista.index("Daniel"))

print("Pepe" in miLista)

miLista1=["María",5,True,78.35]

print(miLista1[:])

miLista1.append("Daniel")

print(miLista1[:])

miLista1.remove("Daniel")

print(miLista1[:])

miLista1.pop()

print(miLista1[:])

miLista2=["Zurisadai","Betsabe"]

miLista3=miLista1+miLista2

print(miLista3[:])


miLista2=["Zurisadai","Betsabe"] * 3

print(miLista2[:])

