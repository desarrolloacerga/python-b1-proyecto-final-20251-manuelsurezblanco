"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""

"""
Módulo principal que lanza el sistema de comida rápida.
"""

#Importo dependencias y de modulos creados
from util.file_manager import CSVFileManager
from util.converter import UserConverter, ProductConverter
from orders.order import Order

class PrepareOrder:
    """
    Lanzamos la clase que controla el programa de comida rápida.
    """
    def __init__(self):
        """Inicializa las listas de cajeros, clientes y productos."""
        self.lista_cajeros = []
        self.lista_clientes = []
        self.lista_productos = []

    def cargar_datos(self):
        """
        Muestro los datos de los CSV indicados.
        """
        print("--- Cargando datos desde archivos CSV ---")
        
        # convierto los usuaris
        convertidor_usuarios = UserConverter()
        
        # 1. Cargo cajeros
        df_cajeros = CSVFileManager("data/cashiers.csv").read()
        self.lista_cajeros = convertidor_usuarios.convert(df_cajeros, "cashier")
        print("\n[Cajeros Registrados]")
        convertidor_usuarios.print(self.lista_cajeros)

        # 2. Cargo clientes
        df_clientes = CSVFileManager("data/customers.csv").read()
        self.lista_clientes = convertidor_usuarios.convert(df_clientes, "customer")
        print("\n[Clientes Registrados]")
        convertidor_usuarios.print(self.lista_clientes)

        # 3. Cargo productos
        convertidor_productos = ProductConverter()
        
        df_hamburguesas = CSVFileManager("data/hamburgers.csv").read()
        self.lista_productos.extend(convertidor_productos.convert(df_hamburguesas, "hamburger"))
        
        df_sodas = CSVFileManager("data/sodas.csv").read()
        self.lista_productos.extend(convertidor_productos.convert(df_sodas, "soda"))
        
        df_bebidas = CSVFileManager("data/drinks.csv").read()
        self.lista_productos.extend(convertidor_productos.convert(df_bebidas, "drink"))
        
        df_happy = CSVFileManager("data/happyMeal.csv").read()
        self.lista_productos.extend(convertidor_productos.convert(df_happy, "happymeal"))
        
        print("\n[Productos cargados]")
        convertidor_productos.print(self.lista_productos)
        print("-" * 60 + "\n")

    def buscar_cajero(self, dni: str):
        """Busca cajero por DNI. Si no existe devuelve None."""
        for cajero in self.lista_cajeros:
            if str(cajero.dni).strip() == dni.strip():
                return cajero
        return None

    def buscar_cliente(self, dni: str):
        """Busca cliente por DNI. Si no existe devuelve None."""
        for cliente in self.lista_clientes:
            if str(cliente.dni).strip() == dni.strip():
                return cliente
        return None

    def buscar_producto(self, id_producto: str):
        """Busca producto por ID. Si no existe devuelve None."""
        for producto in self.lista_productos:
            if str(producto.id).strip() == id_producto.strip():
                return producto
        return None

    def ejecutar_menu(self):
        """Controlo por pantalla los pasos a la hora de pedir los datos de la orden."""

        self.cargar_datos()
        
        print("=== INICIO DE PREPARACIÓN DE LA ORDEN ===")
        
        # Pido cajero y valido su existencia
        cajero_actual = None
        while cajero_actual is None:
            dni_entrada = input("Introduce DNI cajero: ").strip()
            cajero_actual = self.buscar_cajero(dni_entrada)
            if cajero_actual:
                print(f"Cajero seleccionado -> {cajero_actual.name}")
            else:
                print("Cajero no encontrado. Inténtalo de nuevo.")

        # Pido cliente y valido su existencia
        cliente_actual = None
        while cliente_actual is None:
            dni_entrada = input("Introduce DNI cliente: ").strip()
            cliente_actual = self.buscar_cliente(dni_entrada)
            if cliente_actual:
                print(f"Cliente seleccionado -> {cliente_actual.name}")
            else:
                print("Cliente no encontrado. Inténtalo de nuevo.")

        # Inicialización de la Orden de Compra (Inyección de dependencias de actores)
        orden_nueva = Order(cajero_actual, cliente_actual)

        # Entrada interactiva de ítems al carrito
        print("\n--- Selección de productos ---")
        respuesta_usuario = "si"
        
        while respuesta_usuario.lower() == "si":
            id_entrada = input("Introduce product id: ").strip()
            producto_seleccionado = self.buscar_producto(id_entrada)
            
            if producto_seleccionado:
                print(f"Agregado con éxito: {producto_seleccionado.name} ({producto_seleccionado.price} €)")
                orden_nueva.add(producto_seleccionado)
            else:
                print("ID de producto no válido. No se pudo agregar.")
                
            respuesta_usuario = input("¿Quieres agregar otro producto? (si/no): ").strip()

        # Renderizado final del ticket de venta
        orden_nueva.show()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    aplicacion = PrepareOrder()
    aplicacion.ejecutar_menu()