from lesson_builder import LessonBuilder
from lesson import Lesson


class NewStudentLessonBuilder(LessonBuilder):
  """
  Deriva da classe LessonBuilder e executa as etapas definidas nela.
  Corresponde à classe ConcreteBuilder no diagrama UML.
  """

  def __init__(self):
    self.lesson = Lesson()

  def get_lesson(self):
    """
    As invocações de objetos são realizadas aqui.
    Como chamá-lo depende inteiramente do desenvolvedor.
    1-2 valores serão atribuídos para ver a saída.
    """
    self.lesson.id = 1
    self.lesson.name = "Inteligência Artificial - Iniciante a Avançado em 10 Minutos."
    self.lesson.price = 49.99

  def apply_discount(self):
    # Há um desconto de 50% no curso atual para novos alunos aqui.
    self.lesson.discounted_price = self.lesson.price * 0.5

  def add_lesson_note(self):
    self.lesson.lesson_note = "Ei, bem-vindo. Seu código de desconto foi aplicado!"

  def get_result(self):
    return self.lesson