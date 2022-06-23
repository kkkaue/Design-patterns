from veiculos.Veiculo import VeiculoInterface

class Carro(VeiculoInterface):
    def __init__(self, nome_carro: str) -> None:
        self.nome_carro = nome_carro

    def buscar(self, nome) -> None:
        print(f"{self.nome_carro} esta buscando {nome}")

    def parar(self, destino) -> None:
        print(f"{self.nome_carro} chegou ao destino: {destino}")