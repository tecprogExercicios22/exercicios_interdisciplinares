import primo

class Principal():
    """Classe principal"""
    def __init__(self):
        self.valor = primo.Ex1Primo()

    def executar(self):
        """Comandos a serem executados para setar e testar valor"""
        try:
            entrada = int(input("Digite o valor a ser testado se eh primo: "))
        except ValueError:
            print("Valor inválido inserido")
        else:
            self.valor.setNumero(entrada)
            self.valor.ehPrimo()
