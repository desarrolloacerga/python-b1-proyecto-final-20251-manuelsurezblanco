#Importo dependencias  y clases de otros módulos
from datetime import datetime
from users.user import Cashier, Customer
from products.product import Product

class Order:
    """
    Clase principal del sistema. Va asociacida a un cajero, un cliente, 
    una lista de productos y una huella de tiempo.
    """
    def __init__(self, cashier: Cashier, customer: Customer):
        """Inicializa la orden con las clases principales y una lista de productos vacía."""
        self.cashier = cashier
        self.customer = customer
        # Lista vacía para almacenar las lineas de la orden
        self.productos: list[Product] = []
        # Marca de tiempo de cada linea
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add(self, product: Product):
        """Aado un producto al listado de la orden actual."""
        self.productos.append(product)

    def calculateTotal(self) -> float:
        """Calculo el importe total acumulado aplicando redondeo 2 decimales."""
        total = 0.0
        for producto in self.productos:
            total += producto.price
        return round(total, 2)

    def show(self):
        """Desglose completo de la orden."""
        print("\n" + "=" * 60)
        print(f"Fecha/Hora del pedido: {self.fecha_hora}")
        print(f"Hello: {self.customer.describe()}")
        print(f"Was attended by: {self.cashier.describe()}")
        print("-" * 60)
        
        # Recorro cada producto que compone la orden
        for indice, producto in enumerate(self.productos, start=1):
            paquete = producto.foodPackage()
            print(f"Product {indice}: Product - Type: {producto.type()}, Name: {producto.name}, "
                  f"Id: {producto.id}, Price: {producto.price}, Wrapping: {paquete.pack()}, "
                  f"Material: {paquete.material()}")
                  
        print("-" * 60)
        print(f"Total price: {self.calculateTotal()} €")
        print("=" * 60 + "\n")