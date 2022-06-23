# Contém um método para obter instâncias de classes que implementam a interface Iterator.
# Dessa forma, podemos obter instâncias de classes que implementam as várias interfaces Iterator.
# Corresponde à interface Agregada no diagrama UML.
from abc import ABC, abstractmethod

class EmployeeAggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass