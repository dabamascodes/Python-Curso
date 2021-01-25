#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:03:48 2020

@author: danielbarraza
"""

"""
Condicional If Else Elif
"""

print("Verificación de acceso")

nota_alumno=int(input("Introduce tu nota, por favor: "))


if nota_alumno<5:
    print("Insuficiente")
elif nota_alumno<6:
    print("Suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Notable")
else:
    print("Sobresaliente")

print("El Programa ha Finalizado")