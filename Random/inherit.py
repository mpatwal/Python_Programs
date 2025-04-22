class person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def display(self):
        print(self.n, "\n", self.a)


class teacher(person):
    def __init__(self, name, age, exp):
        super().__init__(name, age)
        self.e = exp

    def display(self):
        print("\n", self.exp)


class student(person):
