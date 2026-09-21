from sorteio import Ex2Sorteio

class Principal():
    """Classe principal que irá executar o programa"""
    def __init__(self):
        self.sorteio = Ex2Sorteio()

    def executar(self):
        self.sorteio.adivinhar()
        self.sorteio.getTentativas()
