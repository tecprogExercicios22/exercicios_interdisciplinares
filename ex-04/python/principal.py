from desafio import Desafio

class Principal():
    def __init__(self):
        self.guess = Desafio()

    def executar(self):
        self.guess.tentativa()
