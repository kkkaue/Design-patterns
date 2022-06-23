# É a interface onde são definidas as operações para navegar na coleção.
# Mover para o próximo elemento, como se o próximo elemento existe ou não.
# Corresponde à interface Iterator no diagrama UML.
# Ao fornecer uma estrutura genérica, é usado em muitos lugares.
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def get_current_item(self):
        pass