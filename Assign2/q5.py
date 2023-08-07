class Class_1:
    def __init__(self, str_):
        self.str_ = str_

    def getString(self):
        print("Enter string:")
        self.str_ = input()
        return
    def printString(self):
        return print(self.str_)

x = Class_1("Salom, Doston")
x.printString()