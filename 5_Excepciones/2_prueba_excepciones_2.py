#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:07:14 2020

@author: danielbarraza
"""

"""
EXCEPCIONES
    
    * Capturas de varias excepciones
    
    * Cláusula finally
"""

# def divide():
#     try:
#         opt1=(float(input("Introduce el primer número: ")))
#         opt2=(float(input("Introduce el segundo número: ")))
#         print("La división es: " + str(opt1/opt2))
#     except ValueError:
#         print("El valor introducido es erróneo")
#     except ZeroDivisionError:
#         print("No se puede dividir entre 0")
#
#     print("Cálculo finalizado")
#
# divide()

#=============================================================================

# def divide():
#     try:
#         opt1=(float(input("Introduce el primer número: ")))
#         opt2=(float(input("Introduce el segundo número: ")))
#         print("La división es: " + str(opt1/opt2))
#     except:
#         print("Ha ocurrido un error")
#     print("Cálculo finalizado")
#
# divide()

#=============================================================================

# def divide():
#     try:
#         opt1=(float(input("Introduce el primer número: ")))
#         opt2=(float(input("Introduce el segundo número: ")))
#         print("La división es: " + str(opt1/opt2))
#     except ValueError:
#         print("El valor introducido es erróneo")
#     except ZeroDivisionError:
#         print("No se puede dividir entre 0")
#     finally:
#         print("Cálculo finalizado")
#
# divide()

#=============================================================================

# def divide():
#     try:
#         opt1=(float(input("Introduce el primer número: ")))
#         opt2=(float(input("Introduce el segundo número: ")))
#         print("La división es: " + str(opt1/opt2))
#
#     finally:
#         print("Cálculo finalizado")
#
# divide()

#=============================================================================

def divide():
    try:
        opt1=(float(input("Introduce el primer número: ")))
        opt2=(float(input("Introduce el segundo número: ")))
        print("La división es: " + str(opt1/opt2))
    #finally:
    print("Cálculo finalizado")
    
divide()