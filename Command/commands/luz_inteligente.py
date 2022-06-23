class LuzInteligente:
    isOn = False
    intensidade = 50

    def __init__ (self, nome):
        self.nome = nome
        pass

    def getStatus(self) -> str:
        if (self.isOn == False):
            return 'Desligada'
        else:
            return 'Ligada'
    
    def ligada(self) -> bool:
        self.isOn = True
        print(f'{self.nome} agora está {self.getStatus()}')
        return self.isOn

    def desligada(self) -> bool:
        self.isOn = False
        print(f'{self.nome} agora está {self.getStatus()}')
        return self.isOn

    def aumentarIntensidade(self) -> int:
        if (self.intensidade >= 100): 
            return self.intensidade
        self.intensidade += 1
        return self.intensidade
    
    def diminuirIntensidade(self) -> int:
        if (self.intensidade <= 0): 
            return self.intensidade
        self.intensidade -= 1
        return self.intensidade