from abc import ABC
"""
    Fornece uma interface comum para comunicação.
    Mantém uma instância pois a comunicação será feita pelo Mediador.
    Inclui os recursos de recebimento e envio de mensagens.
    Corresponde à estrutura Colleague no diagrama UML.
"""
class User(ABC):
    u_id: int
    name: str

    def __init__(self, chat_room_mediator):
        self._chat_room_mediator = chat_room_mediator

    def receive_message(self, message: str):
        print(f"{self.name} received new message. Message: {message}")

    def send_message(self, message: str, user_id):
        print(f"{self.name} send new message to: {user_id} id user.")
        self._chat_room_mediator.send_message(message, user_id)