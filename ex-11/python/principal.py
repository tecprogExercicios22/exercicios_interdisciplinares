from fatorador import Fatorador

class Principal():
    def __init__(self):
        self.num_fatorar = Fatorador()

    def executar(self):
        self.num_fatorar.setNum()
        self.num_fatorar.fatorador()
        self.num_fatorar.printFatores()
