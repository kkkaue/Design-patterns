from abstract_chat_room_mediator import AbstractChatRoomMediator
from chat_user import ChatUser
"""
    Implementa a interface do Mediador (IChatRoomMediator).
    Coordena a comunicação entre objetos Colleague (User).
    Corresponde à estrutura ConcreteMediator no diagrama UML.
"""
class ChatRoomMediator(AbstractChatRoomMediator):

    def __init__(self):
        self._user_dictionary = {}

    def send_message(self, message: str, user_id: int):
        user: ChatUser = self._user_dictionary[user_id]
        user.receive_message(message)

    def add_user_in_room(self, user: ChatUser):
        self._user_dictionary[user.u_id] = user