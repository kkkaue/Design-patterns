from delivery_factory import DeliveryFactory
from delivery_context import deliveryContext

factory = DeliveryFactory()

deliveryContext(factory, 'Luiz', '20A', 'Av Brasil', 'SP')
deliveryContext(factory, 'Helena', '20A', 'Av Brasil', 'SP')
deliveryContext(factory, 'Joana', '502', 'Av Brasil', 'SP')

deliveryContext(factory, 'Ana', '2', 'rua A', 'BH')
deliveryContext(factory, 'João', '501', 'rua B', 'RJ')
print("")
print(factory.getLocations())