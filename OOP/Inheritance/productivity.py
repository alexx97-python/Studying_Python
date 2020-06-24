class ProductivitySystem:

    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('No role_type that meets provided role_id')
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('======================')
        for employee in employees:
            employee.perform_duties(hours)
        print('')


class ManagerRole:

    def perform_duties(self, hours):
        return f'screams and yells for {hours} hour.'


class SecretaryRole:

    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'


class SalesRole:

    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'


class FactoryRole:

    def perform_duties(self, hours):
        return  f'manufactures gadgets for {hours} hours.'

