from ex3array import Ex3ArrayControle

class Principal():
    def __init__(self):
        self.vetor_controle = Ex3ArrayControle()

    def executar(self):
        self.vetor_controle.adicionarNums()
        self.vetor_controle.getMedia()
