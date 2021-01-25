#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:55:34 2020

@author: danielbarraza
"""

"""
TUPLAS ()

Las tuplas son listas INMUTABLES, es decir, no se pueden modificar después
de su creación:

	* No permiten añadir, eliminar, mover elementos etc., (no append, extend, remove).
	* Si permiten extraer porciones, pero el resultado de la extracción es una tupla nueva.
	* No permiten búsquedas (no index).
	* Si permiten comprobar si un elemento se encuentra en la tupla.

Las tuplas respecto a las listas:

	* Más rápidas.
	* Menos espacio (mayor optimización).
	* Formatean Strings.
	* PUEDEN UTILIZARSE COMO CLAVES EN UN DICCIONARIO. (las listas no).
"""

mitupla=("Juan", 13,1,1987)
print(mitupla[1])

milista=list(mitupla)
print(milista)
print(mitupla)

milista1=["Daniel",6,9,1987]

mitupla1=tuple(milista1)
print(milista1)
print(mitupla1)

print("Daniel" in mitupla1)
print(mitupla1.count("Daniel"))
print(len(mitupla1))

#Tupla unitaria
mitupla2=("Barraza",)
print(len(mitupla2))

#Empaquetado de tupla
mitupla3="México",21,9,1821
print(mitupla3)

#Desempaquetado de Tuplas
nombre, dia, mes, agno = mitupla3
print(nombre)
print(agno)
print(mes)
print(dia)

