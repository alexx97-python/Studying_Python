from abc import ABC, abstractmethod
import hr
import productivity


# ABC shows that this is an abstract base class
# with which we actually can't create any object
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None

    # it means that this method should be redefined
    # in new classes where base is Employee (abstract method)


class Manager(Employee, productivity.ManagerRole, hr.SalaryPolicy):

    def __init__(self, id, name, weekly_salary):
            hr.SalaryPolicy.__init__(self, weekly_salary)
            super().__init__(id, name)


class Secretary(Employee, productivity.SecretaryRole, hr.SalaryPolicy):

    def __init__(self, id, name, weekly_salary):
        hr.SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class SalesPerson(Employee, productivity.SecretaryRole, hr.CommissionPolicy):

    def __init__(self, id, name, weekly_salary, commission):
        hr.CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)


class FactoryWorker(Employee, productivity.FactoryRole, hr.HourlyPolicy):

    def __init__(self, id, name, hours_worked, hour_rate):
        hr.HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)
