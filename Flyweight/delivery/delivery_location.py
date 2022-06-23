from delivery_flyweight_interface import DeliveryFlyweight
from delivery_types import DeliveryLocationData

class DeliveryLocation(DeliveryFlyweight):
    def __init__(self, street, city) -> DeliveryLocationData:
        self.street = street
        self.city = city

    def delivery(self, nome, numero) -> None:
        print(f'Entrega para {nome}')
        print(f'Em', self.street, self.city)
        print(f'Número: {numero}')
        print('-------------------')
