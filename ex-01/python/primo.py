class Ex1Primo():
    """Classe para verificar se um número é primo ou não"""

    def __init__(self):
        """Aterra o valor da variável"""
        self.numero = -1

    def setNumero(self, valor):
        """Set para indicar novo valor a ser testado"""
        if(valor < 0):
            print("Valores negativos não são aceitos")
            return
        self.numero = valor

    def ehPrimo(self):
        """Testa para saber se numero eh primo"""
        if(self.numero == -1):
            print("Valor não foi setado")
        elif(self.numero <= 1):
            print(f"{self.numero} nao eh primo")
        else:
            for i in range(2, int(self.numero**0.5) + 1):
                if(self.numero % i == 0):
                    print(f"{self.numero} nao eh primo")
                    return
            print(f"{self.numero} eh primo")

        

