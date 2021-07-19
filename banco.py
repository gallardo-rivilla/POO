'''
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.

Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.

La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
'''
#daleee
# creamos la clase banco
class Banco:
	# inicializamos
	def __init__(self):
		self.cliente1=Cliente("Ivan")
		self.cliente2=Cliente("Marcos")
		self.cliente3=Cliente("Juan")
 #prueba de cambio añadido
	# función para operar
	#prueba 2222
	# otro cambio
	# si o si
	def operacion(self):
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente1.extraer(400)
 
	# función para obtener los depósitos totales
	def depositos(self):
		total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
 
 
 
# creamos la clase Cliente
class Cliente:
   
    
	# inicializamos
	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0
 #TODO1 Ejemplo de comentario con TODO

	# función para depositar dinero
	def depositar(self,cantidad):
		self.cantidad+=cantidad
 
	# función para extraer dinero
	def extraer(self,cantidad):
		self.cantidad-=cantidad
 
	# función para obtener el total de dinero
	def devolver_cantidad(self):
		return self.cantidad
 
	# función para imprimir los datos del cliente
	def imprimir(self):
    #FIXME esto debe arreglarse
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
 
 
# bloque principal
banco1=Banco()
#TODO2 Ejemplo de comentario con TODO
banco1.operacion()
banco1.depositos()