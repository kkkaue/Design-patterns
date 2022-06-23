from delivery_factory import DeliveryFactory

def deliveryContext(factory = DeliveryFactory, nome = str, numero = str, street = str, city = str) -> None:
    location = factory.makeLocation(street, city)
    location.delivery(nome, numero)