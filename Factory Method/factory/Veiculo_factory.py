from veiculos.Veiculo import VeiculoInterface
from abc import ABC, abstractmethod

class VeiculoFactory(ABC):
    #Factory Method
    @abstractmethod
    def getVeiculo(self, nome_carro) -> VeiculoInterface:    
        pass

    def buscar(self, nome, nome_carro) -> VeiculoInterface:
        carro = self.getveiculo(nome_carro)
        carro.buscar(nome)
        return carro


