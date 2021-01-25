#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:24:05 2020

@author: danielbarraza
"""

"""
DICCIONARIOS {}

Estructura de datos que nos permite almacenar valores de diferente tipo
(enteros, cadenas de texto, decimales) e incluso listas y otros diccionarios.

La principal característica de los diccionarios es que los datos se almacenan
asociados a una clave de tal forma que se crea una asociación de tipo
CLAVE : VALOR para cada elemento almacenado.

Los elementos almacenados no están ordenados. El orden es indiferente
a la hora de almacenar información en un diccionario.
"""

midiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}

print(midiccionario["Francia"])
print(midiccionario["España"])
print(midiccionario)

midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)

del midiccionario["Reino Unido"]
print(midiccionario)

midiccionario={"Alemania":"Berlín", 23:"Jordan","Mosqueteros":3}
print(midiccionario)

mitupla=["España","Francia","Reino Unido","Alemania"]
midiccionario1={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(midiccionario1)
print(midiccionario1["Francia"])
print(midiccionario1[mitupla[2]])

midiccionario2={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario2)
print(midiccionario2["Equipo"])
print(midiccionario2["anillos"])

midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(midiccionario3["anillos"])

print(midiccionario3)

print(midiccionario3.keys())

print(midiccionario3.values())

print(len(midiccionario3))