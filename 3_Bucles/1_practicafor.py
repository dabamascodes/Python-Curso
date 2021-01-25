#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:54:31 2020

@author: danielbarraza
"""

"""
BUCLES

DETERMINADOS

	* Se ejecutan UN NúMERO DETERMINADO de veces.
	* Se sabe a priori cuántas veces se va a ejecutar el código del interior del bucle

INDETERMINADOS

	* Se ejecutan UN NúMERO INDETERMINADO de veces.
	* NO SE SABE a priori cuántas veces se va a ejecutar el código del interior del bucle
	* El número de veces que se ejecutará dependerá de las circunstancias durante la ejecución del programa.
"""
"""
for VARIABLE in ELEMENTO A RECORRER:
"""
for i in [1, 2, 3]:
    print("Hola")

for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i)

for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end=" ") #Argumento END nos permite determinar como terminará el Print

#

# =============================================================================

email=False
miEmail=input("Introduce tu dirección de email: ")


for i in miEmail:

    if (i=="@"):

        email=True

if email==True:

    print("Email es correcto")

else:

    print("El email no es correcto")

# =============================================================================

contador=0
miEmail=input("Introduce tu dirección de email: ")


for i in miEmail:

    if i== "@" or i== ".":

        contador=contador+1

if contador>=2:

    print("Email es correcto")

else:

    print("El email no es correcto")

# =============================================================================

for i in range(5):

    #print(i)

    print(f"valor de la variable {i}") #Al poner una "f" estamos indicandole a python que queremos utilizar una notación especial

# =============================================================================

for i in range(5,10):
for i in range(5,50,3):

    #print(i)

    print(f"valor de la variable {i}")

# =============================================================================

valido=False

email=input("Introduce tu email: ")


for i in range(len(email)):

    if email[i]== "@":

        valido=True

if valido==True:

    print("Email es correcto")

else:

    print("El email no es correcto")

# =============================================================================

valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):

    if email[i] == "@":
        valido = True

if valido:

    print("Email es correcto")

else:

    print("El email no es correcto")
