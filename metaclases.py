# Creación de metaclases
# Las metaclases definen las caracteristicas que tendra la clase

# Definimos un clase
class miClase():
    pass


# Creamos una instancia de miClase:
uno = miClase()

# Vemos cual es el tipo de la instancia:
print(type(uno))

# Comrobamos con miClase tiene el tipo de class
print(type(miClase))

miPrueba = type('Prueba', (), {'valor': 10})

print(miPrueba)
print(type(miPrueba))


# En Python las clases son OBJETOS:
def hola():
    class Hola:
        pass
    return Hola

# Ejemplo de Metaclase:

class MiMeta(type):

    '''
    __new__ se ejecuta antes que __init__
    Nos sirve para indicar como deseamos que se lleve a cabo la construccion del objeto
    Como parammetros obtenemos el nombre de la clase
    Su clase base y los atributos
    Al final invocamos el constructor de type y regresamos lo que devuelva

    '''
    def __new__(self,class_name,bases,attrs):
        print("Nombre",class_name)
        print("Base",bases)
        print("Atributos",attrs)

        # Creamos un atributo propio de la metaclase:

        d ={}
        for elemento, valor in attrs.items():
            d[elemento]=valor
        
        d['miatributo']= '55'


        return type(class_name,bases,d)

class miClase(metaclass=MiMeta):
    a=5
    nombre='alfonso'  

    def imprime(self):
        print(self.nombre*self.a)
        print(self.miatributo)   # Imprimimos el atributo que fue definido la Metaclase


objeto1=miClase()

objeto1.imprime()

objeto1.miatributo
