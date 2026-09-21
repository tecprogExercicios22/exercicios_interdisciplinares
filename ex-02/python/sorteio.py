from random import randint

class Ex2Sorteio():
    """Guarda um numero e conta quantas tentativas o usuario usou para descobrir ele"""
    def __init__(self):
        """Inicializa valores das variaveis de tentativas e numero aleatorio"""
        self.tentativas = 0
        self.numero = randint(0, 1000)

    def adivinhar(self):
        """Método para usuario tentar adivinhar o numero aleatorio"""
        entrada = -1
        while(entrada != self.numero):
            self.tentativas += 1
            try:
                entrada = int(input("Digite um valor entre 0 e 1000: "))
            except ValueError:
                print("Valor inválido inserido")
                entrada = -1
                self.tentativas -= 1
            else:
                if(entrada < 0 or entrada > 1000):
                    print("Você inseriu um valor fora dos limites do conjunto")
                    self.tentativas -= 1
                elif(entrada < self.numero):
                    print("Você digitou um número menor, tente novamente")
                elif(entrada > self.numero):
                    print("Você digitou um número maior, tente novamente")
                else:
                    print("Você acertou o número!")

    def getTentativas(self):
        print(f"Você precisou de {self.tentativas} tentativas para acertar o número")
