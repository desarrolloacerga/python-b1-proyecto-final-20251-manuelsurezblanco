#Importamos ABC y abstractmethod para crear una clase abstracta
from abc import ABC, abstractmethod

class User(ABC):
    """
    Clase abstracta que sirve como base para los tipos de usuarios (Cajero y Cliente).
    """
    def __init__(self, dni: str, name: str, age: int):
        # Indico los atributos como en el CSV(los que son comunes a cajeros y clientes)
        self.dni = dni
        self.name = name
        self.age = age

    @abstractmethod
    def describe(self) -> str:
        pass


class Cashier(User):
    """
    Clase concreta que representa a un Cajero.
    """
    def __init__(self, dni: str, name: str, timetable: str, salary: float, age: int):
        super().__init__(dni, name, age)
        # Añadimos los atributos específicos del cajero como indica en el CSV
        self.timetable = timetable
        self.salary = salary

    def describe(self) -> str:
        """
        Devuelve una cadena de texto cmo se indica
        en el ejemplo de la salida de la consola.
        """
        return f"Cashier - Name: {self.name}, DNI: {self.dni}, Timetable: {self.timetable}, Salary: {self.salary}."


class Customer(User):
    """
    Clase concreta que representa a un Cliente.
    """
    def __init__(self, dni: str, name: str, age: int, email: str, postal_code: str):
        super().__init__(dni, name, age)
        # Añadimos los atributos específicos del cliente como indica en el CSV
        self.email = email
        self.postal_code = postal_code

    def describe(self) -> str:
        """
        Retornamos una cadena de texto como se pide en el ejemplo de la salida de la consola.
        """
        return f"Customer - Name: {self.name}, DNI: {self.dni}, Age: {self.age}, Email: {self.email}, Postal Code: {self.postal_code}"