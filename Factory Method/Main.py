from factory.Carro_factory import CarroFactory
from factory.Moto_factory import MotoFactory
from factory.Veiculo_factory import VeiculoFactory

#    carroFactory = CarroFactory()
#    fusca = carroFactory.getVeiculo('Fusca')
#    fusca.buscar('Ana')
#    fusca.parar()

 #   motoFactory = MotoFactory()
  #  bis = motoFactory.getVeiculo('bis')
 #   bis.buscar('alex')
  #  bis.parar()

def menu():
    nome = input("Qual o seu nome?\n")
    destino = input("Qual o seu destino?\n")
    veiculo = input("Qual o meio de transporte? (Carro/Moto)\n")
    if (veiculo == 'Carro') or (veiculo == 'carro'):
        carroFactory = CarroFactory()
        carro = carroFactory.getVeiculo(carroFactory.randomNamevehicle())
        print("Procurando motorista...")
        print("Motorista encontrado")
        carro.buscar(nome)
        carro.parar(destino)
    elif (veiculo == 'Moto') or (veiculo == 'moto'):
        motoFactory = MotoFactory()
        moto = motoFactory.getVeiculo(motoFactory.randomNamevehicle())
        print("Procurando motorista...")
        moto.buscar(nome)
        moto.parar(destino)
    else:
        print("Transporte inexistente ou Erro de digitação")

menu()