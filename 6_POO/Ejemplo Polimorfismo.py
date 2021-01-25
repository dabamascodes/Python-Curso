#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 04:41:28 2020

@author: danielbarraza
"""


class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion:
    
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

# miVehiculo=Moto()

# miVehiculo.desplazamiento()

# miVehiculo2=Coche()

# miVehiculo2.desplazamiento()

# miVehiculo3=Camion()

# miVehiculo3.desplazamiento()
        
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
# miVehiculo=Camion()
#miVehiculo=Coche()
miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)