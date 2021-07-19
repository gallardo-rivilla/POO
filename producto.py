class Producto:

    def __init__(self,codigo,nombre,precio):
        self.__codigo=codigo # Atributo privado, no se puede acceder desde fuera de la clase
        self.__nombre=nombre
        self.__precio=precio

    @property # Llamamos al atributo privado es como un getter 
    def codigo(self):
        return self.__codigo

    @codigo.setter ## 
    def codigo(self,valor):
        self.__codigo = valor
        
    @property # Llamamos al atributo privado es como un get
    def nombre(self):
        return self.__nombre

    @codigo.setter
    def nombre(self,valor):
        self.__nombre = valor

    @property # Llamamos al atributo privado es como un get
    def precio(self):
        return self.__nombre

    @codigo.setter
    def precio(self,valor):
        self.precio = valor


    def calcular_total(self,unidades):
        return self.precio * unidades


    def __str__ (self):
        return 'Codigo: ' + str(self.__codigo)  + ', Nombre: ' +  str(self.__nombre)  + ', Precio: ' + str(self.__precio)

p1 = Producto(1,'Producto 1', 5)
p2 = Producto(2,'Producto 2', 10)
p3 = Producto(3,'Producto 3', 20)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))

class Pedido:

    def __init__(self, productos,cantidades):
        self.__productos = []
        self.__cantidades = []

    def anadir_producto(self, producto, cantidad):
        if not isinstance(producto,Producto):
            raise Exception("anadir_producto:producto debe ser de la clase producto")

        if not isinstance(cantidad,int):
            raise Exception("anadir_producto:cantidad debe un numero")
      
        if cantidad <0:
            raise Exception("anadir_producto:cantidad debe mayor 0")
      
        if producto in self.__productos:
           indice = self.__productos.index(producto)
           self.__cantidades[indice]=self.__cantidades[indice]+ cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self,producto):
         if not isinstance(producto,Producto):
                raise Exception("eliminar_producto:producto debe ser de la clase producto")

         if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos.index(indice)
            del self.__cantidades.append(indice)

         else:
             raise Exception("Eliminar_producto:producto no existe.")


    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__productos,self.__cantidades):
            total = total + p.calcular_total(c)

        return total


    def mostrar_pedido(self):
        for (p,c) in zip(self.__productos,self.__cantidades):
            print("Producto: ", p.nombre, " Cantidad:  " + str(c))

productos = [p1,p2,p3]
cantidades = [5,13,2]

# pedido = Pedido(productos,cantidades)
pedido = Pedido()

try:

    pedido.anadir_producto(p1,5)
    pedido.anadir_producto(p2,10)
    pedido.anadir_producto(p3,20)

    print("Total pedido: " +  str(pedido.total_pedido()))

    pedido.mostrar_pedido()
    pedido.eliminar_producto(p1)

    print("Total pedido: " +  str(pedido.total_pedido()))

    pedido.mostrar_pedido()


except Exception as e:
    print(e)


#print("Total pedido: " +  str(pedido.total_pedido()))