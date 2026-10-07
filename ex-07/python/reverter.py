class Reversor():
    def __init__(self):
        self.string = ""
        self.rstring = ""

    def setString(self):
        self.string = str(input("Digite a string que será revertida: "))

    def revert(self):
        self.rstring = self.string[::-1]

    def getRstring(self):
        return self.rstring

    def getString(self):
        return self.string
