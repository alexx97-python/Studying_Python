class Dog():

    def __init__(self, name, age):
        """ Initialization of attributes """
        self.name = name
        self.age = age
        print("The object of Dog class was created")

    def sit(self):
        """When there is command - dog sit down"""
        print(self.name.title() + ' is sitting down.')

    def jump(self):
        """ The dog will jump according to the commands"""
        print(self.name.title() + " is jumping.")


my_dog = Dog(name='Topic', age=4)
my_dog_2 = Dog(name='Nick', age=7)

print(my_dog.age)
print(my_dog_2.name)
my_dog.jump()