class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
        return

    def set_height(self, new_height):
        self.height = new_height
        return

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if int(self.width) > 50 or int(self.height) > 50:
            return "Too big for picture."

        line = '*' * self.width + '\n'
        picture = line * self.height
        return picture

    def get_amount_inside(self, shape):
        answer = self.get_area() // shape.get_area()
        return answer

    def __str__(self):
        line = "Rectangle(width={}, height={})".format(self.width, self.height)
        return line


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        line = "Square(side={})".format(self.height)
        return line