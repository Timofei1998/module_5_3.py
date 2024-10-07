class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for floor in range(1, new_floor+1):
            print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        """должен возвращать True, если количество этажей одинаковое у self и у other."""
        if not isinstance(other, House):
            return False
        return other.number_of_floors == self.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors < self.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors <= self.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors > self.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors >= self.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            return False
        return other.number_of_floors != self.number_of_floors

    def __add__(self, value):
        """- увеличивает кол-во этажей на переданное значение value, возвращает сам объект self."""
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        """- работают так же как и __add__ (возвращают результат его вызова)."""
        return self + value

    def __iadd__(self, value):
        """- работают так же как и __add__ (возвращают результат его вызова)."""
        return self + value


def test2():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__
"""
Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
"""

def test1():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))

"""
Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20
"""


def main():
    h1 = House('пещера', -2)
    h1.go_to(0)
    h1.go_to(-1)
    h1.go_to(-2)
    h1.go_to(-3)

    h2 = House('_______________', 0)
    h2.go_to(1)
    h2.go_to(0)
    h2.go_to(-1)
    h2.go_to(-100)

    h3 = House('', 2)
    h3.go_to(0)
    h3.go_to(1)
    h3.go_to(2)
    h3.go_to(3)


#test1()
test2()
#main()