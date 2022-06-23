from commands.luz_inteligente import LuzInteligente
from commands.command import CommandInterface

class LigarLuzCommand(CommandInterface):
    def __init__(self, luz: LuzInteligente):
        self.luz = luz
        pass
    
    def executar(self) -> None:
        self.luz.ligada()

    def desfazer(self) -> None:
        self.luz.desligada()