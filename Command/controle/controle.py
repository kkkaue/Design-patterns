from commands.command import CommandInterface

class Controle() :
    commands = {str : CommandInterface}

    def adicionarCommand(self, nome_botao, command):
        self.commands[nome_botao] = command

    def executarCommand(self, nome_botao):
        self.commands[nome_botao].executar()
    
    def desfazerCommand(self, nome_botao):
        self.commands[nome_botao].desfazer()