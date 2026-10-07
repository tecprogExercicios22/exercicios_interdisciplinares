from reverter import Reversor

class Principal():
    def __init__(self):
        self.stringRevertida = Reversor()

    def executar(self):
        self.stringRevertida.setString()
        self.stringRevertida.revert()
        print(f"String revertida:\n\t{self.stringRevertida.getRstring()}")
