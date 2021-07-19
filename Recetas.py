'''
Script que utilice el menu de una clase Receta dentro de la cual
habrá una lista de ingredientes. Cada ingrediente tendrá como atributos
los siguientes:

- Nombre
- Cantidad
- Unidad de medida

La clase Receta además de contener un menú y una lista de ingredientes
deberá tener un nombre y una lista de pasos o intrucciones asi como los
siguientes comportamientos:

- Agregar ingrediente
- Consultar ingredientes
- Agregar Paso
- Consultar Pasos

'''
import os

class Receta:
    # Declaramos las constantes:
    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASOS = 4
    OPC_SALIR = 0

    def __init__(self, nombre=''):
        self._nombre= nombre
        self._ingredientes = []
        self._pasos = []

    def __str__(self):
        s = f'               {self.nombre}\n'
        s += 'Ingredientes: '
        for ingrediente in self.ingredientes:
            s += f'{ingrediente}\n'

        s += '\nPasos: \n'

        for in, paso in enumerate(self.pasos):
            s += f'{i+1}. {paso}\n'

       

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    @property
    def ingredientes(self):
        return self._ingredientes
    @nombre.setter
    def ingredientes(self,valor):
        self._ingredientes = valor
    @nombre.deleter
    def ingredientes(self):
        del self._ingredientes

    @property
    def pasos(self):
        return self._pasos
    @nombre.setter
    def pasos(self,valor):
        self._pasos = valor
    @nombre.deleter
    def pasos(self):
        del self._pasos

    def menu(self):
        continuar = True
        os.system('cls') # Limpiamos la pantalla
        while continuar:
            print(f'''  {self._nombre}
            {self.OPC_AGREGAR_INGREDIENTE}) Agregar Ingrediente
            {self.OPC_CONSULTAR_INGREDIENTES}) Consultar Ingrediente
            {self.OPC_AGREGAR_PASO}) Agregar Paso
            {self.OPC_CONSULTAR_PASOS}) Consultar Pasos
            {self.OPC_SALIR}) Salir ''')

            opc = int(input("Selecciona una opción:"))
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregar_ingrediente()
            elif opc == self.OPC_CONSULTAR_INGREDIENTES:
                self.consultar_ingrediente()
            elif opc == self.OPC_AGREGAR_PASO:
                self.agregar_paso()
            elif opc == self.OPC_CONSULTAR_PASOS:
                self.consultar_pasos()
            elif opc == self.OPC_SALIR:

                 continuar = False
            else:
                print("Opción no válida...")
                input("Presiona enter para continuar") 

        print("Nos vemos...")

    def agregar_ingrediente(self):
        continuar = True
        while continuar:
            os.system('cls')
            print("           Agregar ingrediente:")
            nombre = input("Nombre: ")
            cantidad = -1
            while cantidad <=0:
                cantidad = input("Cantidad:")
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input('Unidad de medida:')
            ingrediente = Ingrediente(nombre,cantidad,unidad)
            self.ingredientes.append(ingrediente)
            respuesta = input("¿Deseas agregar otro ingrediente? (s/n)")
            if respuesta !='s' and respuesta != 'S':
                continuar=False

    def consultar_ingrediente(self):
        os.system('cls')
        print("              Ingredientes:")
        if len(self.ingredientes) == 0:
            print("no hay ingredientes registrados...")
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')

    def agregar_paso(self):
        continuar = True
        while continuar:
            os.system('cls')
            print("           Agregar paso:")
            paso = input("Paso: ")
            self.pasos.append(paso)
            respuesta = input("¿Deseas agregar otro paso? (s/n)")
            if respuesta !='s' and respuesta != 'S':
                continuar=False

    def consultar_pasos(self):
        os.system('cls')
        print("              Consultar Pasos:")
        if len(self.pasos) == 0:
            print("no hay pasos registrados...")
        else:
            for i, paso in enumerate(self.pasos):
                print(f'{i+1}.{paso}')