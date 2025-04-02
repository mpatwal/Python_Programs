# required argument or positional argument #
def test(name, age):
    print("name : ", name)
    print("age : ", age)


test(10, 'x')

# keyword argument


def test(name, age):
    print("name : ", name)
    print("age : ", age)


test(age=10, name='x')

# default argument


def test(name='x', age='10'):
    print("name : ", name)
    print("age : ", age)


test('a')

# varible-length argument


def test(name, roll, *subject):
    print("name : ", name)
    print("roll_no : ", roll)
    for i in subject:
        print(i)


test('riya', 2, 'x', 'y', 'z')
