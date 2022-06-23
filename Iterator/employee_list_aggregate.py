# Implementa a interface Aggregate (IEmployeeAggregate) e gera uma instância da classe que implementa a interface Iterator.
# As referências a valores são encontradas aqui.
# Corresponde à classe ConcreteAggregate no diagrama UML.
from employee_aggregate import EmployeeAggregate
from employee_iterator import EmployeeIterator
from employee import Employee

class EmployeListAggregate(EmployeeAggregate):
    def __init__(self):
        self._employees = []

    def add(self, employee: Employee):
        self._employees.append(employee)

    def count(self):
        return len(self._employees)

    def get(self, index: int):
        return self._employees[index]

    def create_iterator(self):
        return EmployeeIterator(self)