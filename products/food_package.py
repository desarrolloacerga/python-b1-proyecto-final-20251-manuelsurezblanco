# Importamos ABC y abstractmethod para definir la clase abstracta.
from abc import ABC, abstractmethod

class FoodPackage(ABC):
    """Clase abstracta que define el tipo de empaque de un alimento."""
    
    @abstractmethod
    def pack(self) -> str:
        """Devuelve el tipo específico de paquete."""
        pass
        
    @abstractmethod
    def material(self) -> str:
        """Devuelve el material del paquete."""
        pass
      
    def describe(self):
        """Devolvemos una despcripción del paquete y su material."""
        return f"Empaque: {self.pack()} , Material: {self.material()}"


class Wrapping(FoodPackage):
    """Envolturas de papel/aluminio."""
    
    def pack(self) -> str:
        return "Food Wrap Paper"
        
    def material(self) -> str:
        return "Aluminium"


class Bottle(FoodPackage):
    """Para botellas."""
    
    def pack(self) -> str:
        return "Bottle"
        
    def material(self) -> str:
        return "Plastic"


class Glass(FoodPackage):
    """Para vasos."""
    
    def pack(self) -> str:
        return "Glass"
        
    def material(self) -> str:
        return "Carton"


class Box(FoodPackage):
    """Para cajas."""
    
    def pack(self) -> str:
        return "Box"
        
    def material(self) -> str:
        return "Cardboard"