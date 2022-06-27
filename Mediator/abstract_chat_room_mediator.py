from abc import ABC, abstractmethod
"""
    Colleague (User) define a interface de comunicação entre objetos.
    Corresponde à interface Mediator no diagrama UML.
"""
class AbstractChatRoomMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user_id: int):
        pass

    @abstractmethod
    def add_user_in_room(self, user):
        pass