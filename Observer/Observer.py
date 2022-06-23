class Subject:
  # Representa o que está sendo observado
	def __init__(self):
    # cria uma lista de observadores vazia
		self._observers = []

	def notify(self, modifier = None):
    # Alerta os observers
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):
    # Se o observer não estiver na lista, anexe-o à lista
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):
    # Remove o observador da lista de observadores
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

class Data(Subject):
  # monitora o objeto
	def __init__(self, name =''):
		Subject.__init__(self)
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		self.notify()

class HexalViewer:
  # atualiza o Hexal viewer
	def update(self, subject):
		print('HexalViewer: O sujeito {} contém o dado 0x{:x}'.format(subject.name, subject.data))

class OctalViewer:
  # atualiza o Octal viewer
	def update(self, subject):
		print('OctalViewer: O sujeito ' + str(subject.name) + ' contém o dado '+str(oct(subject.data)))

class DecimalViewer:
  # atualiza o Decimal viewer
	def update(self, subject):
		print('DecimalViewer: O sujeito % s contém o dado% d' % (subject.name, subject.data))

if __name__ == "__main__":

	obj1 = Data('Dado 1')
	obj2 = Data('Dado 2')

	view1 = DecimalViewer()
	view2 = HexalViewer()
	view3 = OctalViewer()

	obj1.attach(view1)
	obj1.attach(view2)
	obj1.attach(view3)
	obj2.attach(view1)
	obj2.attach(view2)
	obj2.attach(view3)

	obj1.data = 10
	obj2.data = 15
