# Implementa a interface do Iterator e os métodos para percorrer a coleção.
# As operações de roaming nos dados serão realizadas aqui.
# Funciona com a classe ConcreteAggregate (EmployeeListAggregate)
from iterator import Iterator

class EmployeeIterator(Iterator):
    def __init__(self, employee_list_aggregate):
        self._employee_list_aggregate = employee_list_aggregate
        self._current_index = 0

    def has_next(self):
        """
        SYB: Para ver a função da função has_next mais claramente
        aqui está a versão python completa desta função:

          if(len(self._employee_list_aggregate.count() > self._current_index)):
              retornar Verdadeiro
          retorna falso

        No entanto, é possível fazer esse controle 
        em uma única linha com um estilo de escrita pythonico da seguinte forma.
        """
        return self._employee_list_aggregate.count() > self._current_index

    def get_current_item(self):
        current_employee = self._employee_list_aggregate.get(self._current_index)
        self._current_index += 1
        return current_employee