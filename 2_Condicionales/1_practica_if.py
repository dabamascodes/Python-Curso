#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:10:07 2020

@author: danielbarraza
"""

"""
Condicional If
"""

print("Programa de evaluación de notas de alumnos")

nota_alumno=input()

def evaluacion(nota):
    
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))