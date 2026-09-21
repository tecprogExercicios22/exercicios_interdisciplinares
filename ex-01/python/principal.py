import primo

class Principal():
    """Classe principal"""
    def __init__(self):
        self.valor = primo.Ex1Primo()

    def executar(self):
        """Comandos a serem executados para setar e testar valor"""
        self.valor.setNumero(int(input("Digite o valor a ser testado se eh primo: ")))
        self.valor.ehPrimo()
