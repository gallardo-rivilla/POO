
# Cambio de gatos
class Gato:
    '''
    Clase para defirnir Gatos

    '''
# Definimos constantes, atributo estatico:
    especie = "mamífero"


# 1. Método
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[]

# 2. Método
    def verEtapadeVida(self):
        if self.edad>1:
            print(self.nombre,"es adulto")

        else:
            print(self.nombre,"es cachorro")

# 3. Método
    def esAlimentoFavorito(self,alimento):
        return alimento in self.alimentos

 # help(Gato)

# Creo un objeto:
p = Gato("Alfonso",28)
print(p.nombre)

# Añadimos alimento al objeto p
p.alimentos.append(["pescado","pasta"])
print(p.alimentos)

# Llamamos al metodo 2 para el objeto p:
p.verEtapadeVida()

a = Gato("Pepe",1)

print(p.especie)
Gato.especie
