from employee_list_aggregate import EmployeListAggregate
from employee import Employee

if __name__ == '__main__':
    employee_list_aggregate = EmployeListAggregate()
    kaue = Employee(1, "Kauê", "Brandão")
    alex = Employee(2, "Alex", "Nascimento")
    lorena = Employee(3, "Lorena", "Nunes")

    employee_list_aggregate.add(kaue)
    employee_list_aggregate.add(alex)
    employee_list_aggregate.add(lorena)

    print ("Quantidade de funcionários: ",employee_list_aggregate.count(),'\n')

    iterate = employee_list_aggregate.create_iterator()

    while iterate.has_next():
        current_employee: Employee = iterate.get_current_item()
        print(f"{current_employee.first_name} {current_employee.last_name}")
'''
Resultado:
Quantidade de funcionários: 3

Kauê Brandão
alex Nascimento
Lorena Nunes
'''