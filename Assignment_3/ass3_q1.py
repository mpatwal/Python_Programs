# create a class which performs basic calculator operation
class calcultor_operation:
    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        if b == 0:
            print("runtime error")
        else:
            return a/b


c = calcultor_operation()


def menu():
    while True:
        print("1. Addition ")
        print("2. Subtraction ")
        print("3. Multiplication")
        print("4. Division ")
        print("5. Exit ")

        ch = int(input("enter your choice : "))
        if ch == 1:
            a = int(input("enter first number : "))
            b = int(input("enter second number : "))
            print("addition : ", c.add(a, b))
        elif ch == 2:
            a = int(input("enter first number : "))
            b = int(input("enter second number : "))
            print("subtraction :  ", c.sub(a, b))
        elif ch == 3:
            a = int(input("enter first number : "))
            b = int(input("enter second number : "))
            print("multiplication :  ", c.mul(a, b))
        elif ch == 4:
            a = int(input("enter first number : "))
            b = int(input("enter second number : "))
            print("division :  ", c.div(a, b))
        elif ch == 5:
            break
        else:
            print(" enter valid choice ")


menu()
