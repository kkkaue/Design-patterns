from abc import ABC, abstractmethod

class VeiculoInterface(ABC):

    @abstractmethod
    def buscar(self, nome) -> None:
        pass

    @abstractmethod
    def parar(self, destino) -> None:
        pass 