from chat_room_mediator import ChatRoomMediator
from chat_user import ChatUser

if __name__ == '__main__':
  chat_room = ChatRoomMediator()

  # Criação de usuários a serem incluídos na sala de chat.
  # Comunicação com a interface comum do Mediator.
  julio = ChatUser(chat_room)
  # obs: Como o python permite fazer atribuições lado a lado, a definição em uma única linha é exemplificada.
  # não tem diferença com a atribuição feita a um subusuário.
  julio.u_id, julio.name = 1, "Julio"

  kauê = ChatUser(chat_room)
  kauê.u_id = 2
  kauê.name = "Kauê"

  lorena = ChatUser(chat_room)
  lorena.u_id = 3
  lorena.name = "Lorena"

  alex = ChatUser(chat_room)
  alex.u_id = 4
  alex.name = "Alex"

  # Operações de atribuição à lista de usuários no Mediator.
  chat_room.add_user_in_room(julio)
  chat_room.add_user_in_room(kauê)
  chat_room.add_user_in_room(lorena)
  chat_room.add_user_in_room(alex)

  kauê.send_message("oi, tudo bem?", lorena.u_id)
  lorena.send_message("tudo,e você?", kauê.u_id)

  """
    resultado:
    kauê envia nova mensagem para: 3 id user.
    lorena recebeu nova mensagem. Mensagem: oi, tudo bem?
    lorena enviar nova mensagem para: 2 id user.
    kauê recebeu nova mensagem. Mensagem: tudo,e você?
  """