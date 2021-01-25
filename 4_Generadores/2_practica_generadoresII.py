#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:47:53 2020

@author: danielbarraza
"""

"""
YIELD FROM

    * Utilidad: Simplificar el código de los generadores en el caso de utilizar bucles anidados
    
    * Una función GENERADOR nos devuelve un OBJETO GENERADOR en el cual se van almacenando poco a poco diversos elementos.
      Esos elementos pueden ser de una naturaleza diferente: 
      
        * Pueden ser palabras. 
        * Pueden ser valores númericos.
        * Pueden ser listas [].
        * Pueden ser tuplas ().
        * Pueden ser diccionarios {}.
        * Pueden ser objetos de muy diversa índole.
        
      Puede ser que en algunas circunstancias tu desees acceder al interior de uno de esos elementos. Acceder uno a uno de esos subelementos.
"""

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

#===============================================================================

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

#===============================================================================

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))