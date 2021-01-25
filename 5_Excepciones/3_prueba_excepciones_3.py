#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:31:06 2020

@author: danielbarraza
"""

"""
EXCEPCIONES

    * Instrución Raise
    
    * Creación de excepciones propias.
"""

# def evaluaEdad(edad):
#     if edad<0:
#         raise TypeError("No se permiten edades negativas")
#     if edad<20:
#         return "Eres muy joven "
#     elif edad<40:
#         return "Eres joven"
#     elif edad<65:
#         return "Eres maduro"
#     elif edad<100:
#         return "cuidate..."
#
# print(evaluaEdad(15))

#=============================================================================

# def evaluaEdad(edad):
#     if edad<0:
#         raise ZeroDivisionError("No se permiten edades negativas")
#     if edad<20:
#         return "Eres muy joven "
#     elif edad<40:
#         return "Eres joven"
#     elif edad<65:
#         return "Eres maduro"
#     elif edad<100:
#         return "cuidate..."
#
# print(evaluaEdad(15))

#=============================================================================

# def evaluaEdad(edad):
#     if edad<0:
#         raise MiPropioError("No se permiten edades negativas")
#     if edad<20:
#         return "Eres muy joven "
#     elif edad<40:
#         return "Eres joven"
#     elif edad<65:
#         return "Eres maduro"
#     elif edad<100:
#         return "cuidate..."

# print(evaluaEdad(15))

#=============================================================================

import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1=(int(input("Introduce un número: ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")






