from abc import ABC, abstractmethod

class DeliveryFlyweight(ABC):

    @abstractmethod
    def delivery(self, nome, numero) -> None:
        pass
 