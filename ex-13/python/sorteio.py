from random import randint

class MenorQueException(Exception):
    pass

class MaiorQueException(Exception):
    pass

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

                if(entrada < 0 or entrada > 1000):
                    print("Você inseriu um valor fora dos limites do conjunto")
                    self.tentativas -= 1
                elif(entrada < self.numero):
                    raise MenorQueException()
                elif(entrada > self.numero):
                    raise MaiorQueException()
                else:
                    print("Você acertou o número!")

            except MenorQueException:
                print("Você digitou um número menor, tente novamente")
            except MaiorQueException:
                print("Você digitou um número maior, tente novamente")
            except ValueError:
                print("Valor inválido inserido")
                self.tentativas -= 1

    def getTentativas(self):
        print(f"Você precisou de {self.tentativas} tentativas para acertar o número")

