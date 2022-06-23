from veiculos.Veiculo import VeiculoInterface
from veiculos.Moto import Moto
from factory.Veiculo_factory import VeiculoFactory
import random

class MotoFactory(VeiculoFactory):
    def getVeiculo(self, nome_Moto) -> VeiculoInterface:
        return Moto(nome_Moto)

    def randomNamevehicle(self) -> str:
        vet = ['Honda Biz', 'Honda CG 160', 'Honda NXR 160 Bros', 'Honda Pop 110i', 'Honda CB 250F Twister', 'Yamaha XTZ 150 Crosser', 'Yamaha YBR 150 Factor', 'Yamaha Fazer 250 ABS', 'Honda XRE 300', 'Honda PCX']
        return random.choice(vet)
