#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:16:24 2020

@author: danielbarraza
"""

"""
POO (Programación Orientada a Objetos)

    * ¿En qué consiste?
        Trasladar la naturaleza de los objetos de la vida real al código de programación.
        
    * ¿Cuál es la naturaleza de un objeto de la vida real
        Los objetos tienen un ESTADO, un COMPORTAMIENTO (¿qué puede hacer?) y unas PROPIEDADES.
        
    ******************************************************************************************************************************************************************************
    
    CLASE: Módelo donde se redactan las características comunes de un grupo de objetos.
    
    EJEMPLAR DE CLASE / INSTANCIA DE CLASE / OBJETO PERTENECIENTE A UNA CLASE / OBJETO DE CLASE: Objeto o ejemplar perteneciente a una clase.
    
    MODULARIZACIóN: Composición de un programa en una o varias CLASES ó MóDULOS.
    
    ENCAPSULACIóN: Funcionamiento interno de la CLASE  INACCESIBLE Desde fuera.
    
    HERENCIA:
    
    POLIFORMISMO:
"""
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 1: Indroducción a las: Clases, Propiedades, Métodos, Instancias y Objetos.

class Coche():
    # Propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False


    # Métodos (Comportamientos)
    #    Método: Función especial que pertenece a una clase.

    #***********************************************************
    #    def function(self):
    #        pass
    #***********************************************************
    #    self: Objeto perteneciente a la clase

    def arrancar(self):                      # AalMet_2: Lo que recibe "self" por parámetro es el OBJETO: "miCoche"
        self.enmarcha=True                   # AalMet_3: Lo que se convierte realmente en: miCoche.enmarcha=True

    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# INSTANCIA

# Primer Objeto o instancia "miCoche" igualado al nombre de la clase a la cuál pertenece
miCoche = Coche() # <----------------Instanciar una clase

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# PROPIEDADES

# Accediendo a las Propiedades de la clase "Coche()" con nombreObjeto.Propiedad.
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, " ruedas.")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# MéTODOS (Comportamientos)

# Accediendo a los Métodos Acrónimo Auxiliar = AalMet_#
miCoche.arrancar()                           # AalMet_1: Llámamos al Método arrancar(Self): de la CLASE Coche()

print(miCoche.estado())

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 2: DOS INSTANCIAS

class Coche():
    # Propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False


    # Métodos (Comportamientos)
    #    Método: Función especial que pertenece a una clase.

    #***********************************************************
    #    def function(self):
    #        pass
    #***********************************************************
    #    self: Objeto perteneciente a la clase

    def arrancar(self):                      # AalMet_2: Lo que recibe "self" por parámetro es el OBJETO: "miCoche"
        self.enmarcha=True                   # AalMet_3: Lo que se convierte realmente en: miCoche.enmarcha=True

    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# INSTANCIA

# Primer Objeto o instancia "miCoche" igualado al nombre de la clase a la cuál pertenece
miCoche = Coche() # <----------------Instanciar una clase

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# PROPIEDADES

# Accediendo a las Propiedades de la clase "Coche()" con nombreObjeto.Propiedad.
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, " ruedas.")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# MéTODOS (Comportamientos)

# Accediendo a los Métodos Acrónimo Auxiliar = AalMet_#
miCoche.arrancar()                           # AalMet_1: Llámamos al Método arrancar(Self): de la CLASE Coche()

print(miCoche.estado())

print("----------------A Continuación creamos el segundo objeto-----------------")
miCoche2=Coche()
print("El largo del coche es: ", miCoche2.largoChasis)
print("El coche tiene: ", miCoche2.ruedas, " ruedas.")
print(miCoche2.estado())

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#Código 3: DOS INSTANCIAS, + VARIABLE PARA CONTROL

class Coche():
    # Propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False


    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos

        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.ruedas, " rueda(s). Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 4: CONSTRUCTOR:
#
# En POO, es habitual que las características cómunes de los objetos formen parte de algo llamado ESTADO INICIAL,
# Es decir que estas características cómunes sean como de FABRICA, es decir que en cuanto nosotros creamos una INSTANCIA,
# un OBJETO, un EJEMPLAR PERTENECIENTE A UNA CLASE, inmediatamente simplemente después por el hecho de haber creado ese
# OBJETO YA TENGA UN ESTADO INICIAL.
#
# Este ESTADO INICIAL nosotros lo especificamos con lo que se denomina un CONSTRUCTOR.
#
# UN CONSTRUCTOR: Es un método especial que le da ESTADO INICIAL A LOS OBJETOS. Es una forma de especificar claramente
# cual va a ser el ESTADO INICIAL de los OBJETOS que Pertenezcan a una CLASE.

class Coche():

    # Método CONSTRUCTOR DE CLASE
    def __init__(self):
        # Propiedades
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False


    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos

        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.ruedas, " rueda(s). Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 5: SIN ENCAPSULACIóN DE PROPIEDADES: Modificación de Propiedades desde Fuera de la Clase.

class Coche():

    # Método CONSTRUCTOR DE CLASE
    def __init__(self):
        # Propiedades
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False


    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos

        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.ruedas, " rueda(s). Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))

#################################################################################################
# NO DEBERíA DE PERMITIRSE MODIFICAR UNA PROPIEDAD DE CLASE DESDE FUERA DE ELLA
# SI SE ENCAPSULA LA PROPIEDAD DENTRO DE LA CLASE
miCoche2.ruedas=2

#################################################################################################
miCoche2.estado()

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 6 CON ENCAPSULACIóN DE PROPIEDADES
#
# Encapsular: Proteger un(as) propiedad(es) para que no se pueda(n) modificar desde fuera de la CLASE

class Coche():

    # Método CONSTRUCTOR DE CLASE
    def __init__(self):
        # Propiedades: Encapsular Propiedades "self.__Nombre"
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if (self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " rueda(s). Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))

#################################################################################################
# NO DEBERíA DE PERMITIRSE MODIFICAR UNA PROPIEDAD DE CLASE DESDE FUERA DE ELLA
# SI SE ENCAPSULA LA PROPIEDAD DENTRO DE LA CLASE
miCoche2.__ruedas=2

#################################################################################################
miCoche2.estado()

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 7 SIN ENCAPSULACIóN DE MéTODOS

class Coche():

    # Método CONSTRUCTOR DE CLASE
    def __init__(self):
        # Propiedades: Encapsular Propiedades "self.__Nombre"
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene ", self.__ruedas, " rueda(s). Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)


    def chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina =="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

#################################################################################################
# NO DEBERíA DE PERMITIRSE ACCEDER A UN Método DE CLASE DESDE FUERA DE ELLA
# SI SE ENCAPSULA EL MéTODO DENTRO DE LA CLASE

print(miCoche.chequeo_interno())

#################################################################################################
print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()

#################################################################################################
# NO DEBERíA DE PERMITIRSE ACCEDER A UN Método DE CLASE DESDE FUERA DE ELLA
# SI SE ENCAPSULA EL MéTODO DENTRO DE LA CLASE

print(miCoche2.chequeo_interno())

#################################################################################################

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 8 CON ENCAPSULACIóN DE MéTODOS: Aun llamando al Método "__chequeo_interno()" desde fuera de la clase generará un
#
# AttributeError: 'Coche' object has no attribute '__chequeo_interno'

class Coche():

    # Método CONSTRUCTOR DE CLASE
    def __init__(self):
        # Propiedades: Encapsular Propiedades "self.__Nombre"
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene ", self.__ruedas, " rueda(s). Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    # Métodos: Encapsular Métodos: "def __NombreMétodo(self)"
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina =="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

#################################################################################################
# NO DEBERíA DE PERMITIRSE ACCEDER A UN Método DE CLASE DESDE FUERA DE ELLA
# SI SE ENCAPSULA EL MéTODO DENTRO DE LA CLASE

print(miCoche.__chequeo_interno())

#################################################################################################
print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()

#################################################################################################
# NO DEBERíA DE PERMITIRSE ACCEDER A UN Método DE CLASE DESDE FUERA DE ELLA
# SI SE ENCAPSULA EL MéTODO DENTRO DE LA CLASE

print(miCoche2.__chequeo_interno())

#################################################################################################

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Código 9 CON ENCAPSULACIóN DE MéTODOS: YA NO llamando al Método "__chequeo_interno()" desde fuera de la clase
# YA NO generará un
#
# AttributeError: 'Coche' object has no attribute '__chequeo_interno'

class Coche():

    # Método CONSTRUCTOR DE CLASE
    def __init__(self):
        # Propiedades: Encapsular Propiedades "self.__Nombre"
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    # Métodos (Comportamientos)
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene ", self.__ruedas, " rueda(s). Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    # Métodos: Encapsular Métodos: "def __NombreMétodo(self)"
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina =="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



# Instancia
miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("----------------A Continuación creamos el segundo objeto-----------------")

# Instancia
miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

# NOTA:
#
# SE DEBEN ENCAPSULAR PROPIEDADES (Variables) o NO, SE DEBEN ENCAPSULAR MéTODOS (Comportamientos) o NO:
#
# CUANDO TU OBJETO, TU CLASE ASí LO NECESITE.
#
# Y eso depende del comportamiento que quieres que tenga esa CLASE, según tu criterio como Programador.