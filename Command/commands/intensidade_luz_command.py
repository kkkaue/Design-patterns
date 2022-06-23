from commands.luz_inteligente import LuzInteligente
from commands.command import CommandInterface

class IntensidadeLuzCommand(CommandInterface):
    def __init__(self, luz : LuzInteligente):
        self.luz = luz
        pass

    def executar(self) -> None:
        intensidade = self.luz.aumentarIntensidade()
        print(f'Intensidade de {self.luz.nome} é {intensidade}')

    def desfazer(self) -> None:
        intensidade = self.luz.diminuirIntensidade()
        print(f'Intensidade de {self.luz.nome} é {intensidade}')
        