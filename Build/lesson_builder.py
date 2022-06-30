from abc import ABC, abstractmethod
from lesson import Lesson


class LessonBuilder(ABC):
  """
  Fornece a interface abstrata para a criação do objeto da classe Lesson correspondente ao Produto no diagrama UML.
  É definido nos passos a serem feitos.
  """
  lesson: Lesson

  @abstractmethod
  def get_lesson(self):
    pass

  @abstractmethod
  def apply_discount(self):
    pass

  @abstractmethod
  def add_lesson_note(self):
    pass

  @abstractmethod
  def get_result(self):
    pass