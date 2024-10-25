class House:


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors
        else:
            return f'Сравниваемый объект должен принадлежать к классу "House"'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return f'Сравниваемый объект должен принадлежать к классу "House"'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return f'Сравниваемый объект должен принадлежать к классу "House"'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return f'Сравниваемый объект должен принадлежать к классу "House"'


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return f'Сравниваемый объект должен принадлежать к классу "House"'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return f'Сравниваемый объект должен принадлежать к классу "House"'

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return f'Прибавляемое число должно принадлежать к типу "int"'

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = other + self.number_of_floors
            return self
        else:
            return f'Прибавляемое число должно принадлежать к типу "int"'


    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            return f'Прибавляемое число должно принадлежать к типу "int"'



h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК .Акация", 20)

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
