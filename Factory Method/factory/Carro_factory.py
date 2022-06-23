from veiculos.Veiculo import VeiculoInterface
from veiculos.Carro import Carro
from factory.Veiculo_factory import VeiculoFactory
import random

class CarroFactory(VeiculoFactory):
    def getVeiculo(self ,nome_carro) -> VeiculoInterface:
        return Carro(nome_carro)
    
    def randomNamevehicle(self) -> str:
        vet = ['Fusca', 'Mobi', 'Savero', 'Gol quadrado', 'Opala', 'Jeep compass', 'Subaru', 'Ford Escort XR3', 'Ford Del Rey', 'Monza', 'Fiorino']
        return random.choice(vet)
