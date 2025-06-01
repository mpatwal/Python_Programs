def decorator(hello):
    def wrapper():
        print("first line")
        hello()
        print("last line")
    return wrapper


@decorator
def hello():
    print("hi decorator worked successfully")


hello()
