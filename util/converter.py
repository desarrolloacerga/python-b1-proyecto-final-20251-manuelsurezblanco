# uso las importaciones absolutas.
from abc import ABC, abstractmethod
import pandas as pd

# Importo dependencias de otros modulos.
from products.product import Hamburger, Soda, Drink, HappyMeal
from users.user import Cashier, Customer

class Converter(ABC):
    """
    Transformo los datos del datafrae a objeto.
    """
    
    @abstractmethod
    def convert(self, data_frame: pd.DataFrame, *args) -> list:
        """convierto la fila en lista."""
        pass

    def print(self, lista_objetos: list):
        """
        recorro la lista de objetos y los imprimo.
        """
        for objeto in lista_objetos:
            # Si el objeto cuenta con el método describe
            if hasattr(objeto, 'describe') and callable(getattr(objeto, 'describe')):
                # los productos no usan el método describe(), pero los usuarios sí.
                if hasattr(objeto, 'dni'):  
                    print(objeto.describe())
                else:
                    # Formato solicitado para productos
                    paquete = objeto.foodPackage()
                    print(f"Product - Type: {objeto.type()}, Name: {objeto.name}, Id: {objeto.id}, "
                          f"Price: {objeto.price}, Wrapping: {paquete.pack()}, Material: {paquete.material()}")
            else:
                # imprmo el objeto aunue no tenga método describe()
                print(str(objeto))


class UserConverter(Converter):
    """
    Transformo los datos de cajeros y clientes del dataframe a onjeto
    """
    def convert(self, data_frame: pd.DataFrame, tipo_usuario: str) -> list:
        lista_usuarios = []
        
        for _, fila in data_frame.iterrows():
            if tipo_usuario.lower() == "cashier":
                nuevo_usuario = Cashier(
                    dni=str(fila['dni']),
                    name=str(fila['name']),
                    age=int(fila['age']),
                    timetable=str(fila['timetable']),
                    salary=float(fila['salary'])
                )
            elif tipo_usuario.lower() == "customer":
                nuevo_usuario = Customer(
                    dni=str(fila['dni']),
                    name=str(fila['name']),
                    age=int(fila['age']),
                    email=str(fila['email']),
                    postal_code=str(fila['postalcode'])
                )
            else:
                raise ValueError("Tipo de usuario no válido. Use 'cashier' o 'customer'.")
                
            lista_usuarios.append(nuevo_usuario)
            
        return lista_usuarios


class ProductConverter(Converter):
    """
    Convierto los datos de hamburguesas, gaseosas, bebidas y combos del dataframe a objeto
    """
    def convert(self, data_frame: pd.DataFrame, tipo_producto: str) -> list:
        lista_productos = []
        
        for _, fila in data_frame.iterrows():
            id_producto = str(fila['id'])
            nombre_producto = str(fila['name'])
            precio_producto = float(fila['price'])
            
            tipo_normalizado = tipo_producto.lower()
            
            
            if tipo_normalizado == "hamburger":
                nuevo_producto = Hamburger(id=id_producto, name=nombre_producto, price=precio_producto)
            elif tipo_normalizado == "soda":
                nuevo_producto = Soda(id=id_producto, name=nombre_producto, price=precio_producto)
            elif tipo_normalizado == "drink":
                nuevo_producto = Drink(id=id_producto, name=nombre_producto, price=precio_producto)
            elif tipo_normalizado == "happymeal":
                nuevo_producto = HappyMeal(id=id_producto, name=nombre_producto, price=precio_producto)
            else:
                raise ValueError(f"Tipo de producto '{tipo_producto}' desconocido.")
                
            lista_productos.append(nuevo_producto)
            
        return lista_productos