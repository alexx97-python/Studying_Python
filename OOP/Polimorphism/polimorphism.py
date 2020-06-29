
class Shape:
    """
    This is a parent class that is intended to be inherited by other classes
    """

    def calculate_area(self):

        raise NotImplemented('This method does not intend to be used in parent class')


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):

    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


def get_area(input_obj):
    print(input_obj.calculate_area())


shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()

#get_area(shape_obj)  callig this results in Error
get_area(square_obj)
get_area(triangle_obj)

