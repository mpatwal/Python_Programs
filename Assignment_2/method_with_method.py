class ABC:
    def __init__(self, val):
        self.val = val

    def display(self):
        print("value: ", self.val)

    def add(self):
        self.val += 2
        self.display()


obj = ABC(10)
obj.display()
obj.add()
