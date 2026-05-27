#Importo la del módulo abc para definir la clase abstracta Product y sus métodos abstractos.
from abc import ABC, abstractmethod
from products.food_package import FoodPackage, Wrapping, Bottle, Glass, Box


class Product(ABC):
    """Clase abstracta que representa el prodcuto."""
    
    def __init__(self, id: str, name: str, price: float):
        """Inicializa los atributos base desde el CSV."""
        self.id = id
        self.name = name
        self.price = price
        
    @abstractmethod
    def type(self) -> str:
        """devuelvo el tipo de producto."""
        pass
        
    @abstractmethod
    def foodPackage(self) -> FoodPackage:
        """devuelvo el envoltorio específico para el producto."""
        pass

    def describe(self) -> str:
        """devuelvo una descripción formateada del producto."""
        paquete = self.foodPackage()
        return (f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id}, "
                f"Price: {self.price}, Wrapping: {paquete.pack()}, Material: {paquete.material()}.")


class Hamburger(Product):
    """Heredamos de la clase abstracta Product."""
    
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)
        
    def type(self) -> str:
        return "Hamburger"
        
    def foodPackage(self) -> FoodPackage:
        return Wrapping()


class Soda(Product):
    """Heredamos de la clase abstracta Product."""
    
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)
        
    def type(self) -> str:
        return "Soda"
        
    def foodPackage(self) -> FoodPackage:
        return Bottle()


class Drink(Product):
    """Heredamos de la clase abstracta Product."""
    
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)
        
    def type(self) -> str:
        return "Drink"
        
    def foodPackage(self) -> FoodPackage:
        return Glass()


class HappyMeal(Product):
    """Heredamos de la clase abstracta Product."""
    
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)
        
    def type(self) -> str:
        return "HappyMeal"
        
    def foodPackage(self) -> FoodPackage:
        return Box()