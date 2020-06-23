from abc import ABC, abstractmethod


class PayrollSystem:

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('=============')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


# ABC shows that this is an abstract base class
# with which we actually can't create any object
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # it means that this method should be redefined
    # in new classes where base is Employee (abstract method)
    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hours_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


class CommissionEmployee(SalaryEmployee):

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Manager(SalaryEmployee):

    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class Secretary(SalaryEmployee):

    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesPerson(CommissionEmployee):

    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


class FactoryWorker(HourlyEmployee):

    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')
