from math import pi as PI

class Figure:
    side_count = 0

    def __init__(self, color = [0, 0, 0], sides = [], filled = False):
        self.__color = color
        self.__sides = sides
        self.field = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 and isinstance(value, int) for value in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return len(args) == self.side_count and all(isinstance(i, (int, float)) and i > 0 for i in args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    side_count = 1

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]

        super().__init__(color, sides)
        self.__radius = self.get_sides()[0] / (2 * PI)


class Triangle(Figure):
    side_count = 3

    def __init__(self, color = [0, 0, 0], sides = [0, 0, 0], filled = False):
        super().__init__(color, sides, filled)

    def get_square(self):
        p - self.__len__() / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    side_count = 12

    def __init__(self, color = [0, 0, 0], side_length = 1, filled = False):
        sides = [side_length] * 12
        super().__init__(color, sides, filled=filled)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())