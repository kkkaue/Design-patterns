# Interface onde a operação de interpretação é definida.
# Corresponde à interface Expression no diagrama UML.

from abc import ABC, abstractmethod
from context import Context


class JobExpressionInterface(ABC):
  @abstractmethod
  def interpret(self, context: Context):
    pass
