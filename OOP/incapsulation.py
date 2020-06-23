
class Phone():
    username = 'Alex'  # public variable
    __serial_number = "11.22.33"  # private variable
    __how_many_times_turned_on = 0  # private variable

    def call(self):   # public method
        print("Ring-ring!")

    def __turn_on(self):  # private method
        self.__how_many_times_turned_on += 1
        print("Times was turned on: ", self.__how_many_times_turned_on)


my_phone = Phone()  # creating object of class
my_phone.call()  # calling public method
print("The username is: ", my_phone.username)  # calling public variable


my_phone._Phone__turn_on() # accessing private function
my_phone._Phone__serial_number = '44.55.66'  # changing the value of private variable
print("New serial number is ", my_phone._Phone__serial_number )