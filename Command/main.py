from commands.ligar_luz_command import LigarLuzCommand
from commands.luz_inteligente import LuzInteligente
from controle.controle import Controle
from commands.intensidade_luz_command import IntensidadeLuzCommand

# receptor
QuartoLuz = LuzInteligente('Luz do Quarto')
BanheiroLuz = LuzInteligente('Luz do Banheiro')

# command
QuartoLigarLuzCommand = LigarLuzCommand(QuartoLuz);
BanheiroLigarLuzCommand = LigarLuzCommand(BanheiroLuz);
QuartoIntensidadeCommand = IntensidadeLuzCommand(QuartoLuz);

# Controle - Invoker
controle = Controle()
controle.adicionarCommand('botão1', QuartoLigarLuzCommand)
controle.adicionarCommand('botão2', BanheiroLigarLuzCommand)
controle.adicionarCommand('botão3', QuartoIntensidadeCommand)

controle.executarCommand('botão1')
controle.desfazerCommand('botão1')

controle.executarCommand('botão2')
controle.desfazerCommand('botão2')


for x in range(4):
    controle.executarCommand('botão3')

for x in range(2):
    controle.desfazerCommand('botão3')
