class MyFunc:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print(self.input_string.upper())


obj = MyFunc()
obj.get_String()
obj.print_String()
