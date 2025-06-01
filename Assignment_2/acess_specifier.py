class student:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c


s = student(10, 20, 30)
print(s.a)
print(s._b)
# print(s.__c) throw an error that private data members cann't be accessed
