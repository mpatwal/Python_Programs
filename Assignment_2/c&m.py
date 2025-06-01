class student:
    def __init__(self, name):
        self.name = name
        print("Name of the student : ", name)

    def detail(self):
        print("details ")


s = student('riya')
s.detail()
