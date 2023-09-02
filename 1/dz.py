class Item:
    def __init__(self, num: int):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

class Item2:
    def __init__(self, num: int):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __sub__(self, other):
        return self.num - other

    def __mul__(self, other):
        return self.num * other

    def __truediv__(self, other):
        return self.num / other

i1 = Item(5)
i2 = Item2(3)


print(i1+i2)
print(i1-i2)
print(i1*i2)
print(i1/i2)