from permutacao import Permutador

class Principal():
    """Classe principal para executar o programa"""
    def __init__(self):
        self.testePerm = Permutador()

    def executar(self):
        self.testePerm.setNumeros()

        if(self.testePerm.getPermutacoes()):
            print(f"Os números sao permutacoes um do outro")
        else:
            print("Os numeros nao sao permutacoes um do outro")
