

class Celsius:
    """
    This class shows the way of using property as function
    """
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print('Getting value...')
        return self._temperature

    def set_temperature(self, value):
        print('Setting value.')
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


#human = Celsius(37)

#print(human.temperature)

#print(human.to_fahrenheit())

#human.temperature = -300


class Celsius_1:
    """
    This class shows the way of using property decorator
    """
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print('Getting value...')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('Setting value...')
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


human_1 = Celsius_1(36)

print(human_1.temperature)

print(human_1.to_fahrenheit())

cold_thing = Celsius_1(-300)

