from abc import ABCMeta, abstractstaticmethod


class IHandler(metaclass=ABCMeta):
  @abstractstaticmethod
  def set_successor(successor):
    pass

  @abstractstaticmethod
  def handle(amount):
    pass


class Dispenser100(IHandler):
  def __init__(self):
    self._successor = None

  def set_successor(self, successor):
    self._successor = successor

  def handle(self, amount):
    if amount >= 100:
      num = amount // 100
      remainder = amount % 100
      print(f"Dispencin {num} 100$")
      if remainder != 0:
        self._successor.handle(remainder)
    else:
      self._successor.handle(amount)


class Dispenser50(IHandler):
  def __init__(self):
    self._successor = None

  def set_successor(self, successor):
    self._successor = successor

  def handle(self, amount):
    if amount >= 50:
        num = amount // 50
        remainder = amount % 50
        print(f"Dispencin {num} 50$")
        if remainder != 0:
            self._successor.handle(remainder)
    else:
        self._successor.handle(amount)


class Dispenser20(IHandler):
  def __init__(self):
    self._successor = None

  def set_successor(self, successor):
    self._successor = successor

  def handle(self, amount):
    if amount >= 20:
        num = amount // 20
        remainder = amount % 20
        print(f"Dispencin {num} 20$")
        if remainder != 0:
            self._successor.handle(remainder)
    else:
        self._successor.handle(amount)


class Dispenser10(IHandler):
  def __init__(self):
    self._successor = None

  def set_successor(self, successor):
      self._successor = successor

  def handle(self, amount):
    if amount >= 10:
        num = amount // 10
        remainder = amount % 10
        print(f"Dispencin {num} 10$")
        if remainder != 0:
            self._successor.handle(remainder)
    else:
        self._successor.handle(amount)


class Dispenser5(IHandler):
  def __init__(self):
    self._successor = None

  def set_successor(self, successor):
    self._successor = successor

  def handle(self, amount):
    if amount >= 5:
        num = amount // 5
        remainder = amount % 5
        print(f"Dispencin {num} 5$")
        if remainder != 0:
            self._successor.handle(remainder)
    else:
        self._successor.handle(amount)


class Dispenser1(IHandler):
  def __init__(self):
    self._successor = None

  def set_successor(self, successor):
    self._successor = successor

  def handle(self, amount):
    if amount >= 1:
        num = amount // 1
        remainder = amount % 1
        print(f"Dispencin {num} 1$")
        if remainder != 0:
            self._successor.handle(remainder)
    else:
        self._successor.handle(amount)


class ATMDispenserChain:
  def __init__(self):
    self.chain1 = Dispenser100()
    self.chain2 = Dispenser50()
    self.chain3 = Dispenser20()
    self.chain4 = Dispenser10()
    self.chain5 = Dispenser5()
    self.chain6 = Dispenser1()

    self.chain1.set_successor(self.chain2)
    self.chain2.set_successor(self.chain3)
    self.chain3.set_successor(self.chain4)
    self.chain4.set_successor(self.chain5)
    self.chain5.set_successor(self.chain6)


if __name__ == "__main__":
  ATM = ATMDispenserChain()
  while True:
    amount = int(input("Enter a amount: "))
    if amount < 0:
      print("Set Correctly")
      exit()
    ATM.chain1.handle(amount)
