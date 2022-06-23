from veiculos.Veiculo import VeiculoInterface

class Moto(VeiculoInterface):
    def __init__(self, nome_moto: str) -> None:
        self.nome_moto = nome_moto

    def buscar(self, nome) -> None:
        print(f"{self.nome_moto} esta buscando {nome}")

    def parar(self, destino) -> None:
        print(f"{self.nome_moto} você chegou no seu destino: {destino}")