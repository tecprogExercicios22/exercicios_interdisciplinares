from random import randint
from time import sleep, perf_counter

class Desafio():
    """Desenvolve o desafio de tempo"""
    def __init__(self):
        self.numero = randint(0, 1000)
        self.tempo = randint(0, 10)
        self.tempo_digitar = 0

    def tentativa(self):
        print("Prepare-se...")
        sleep(self.tempo)
        print(f"AGORA! - {self.numero}")
        self.lerNum()
        print(f"Você levou {self.tempo_digitar:.3f}s para digitar o número!")

    def lerNum(self):
        leitura = -1
        inicio = perf_counter()
        while(leitura != self.numero):
            try:
                leitura = int(input("Digite o número: "))
            except ValueError:
                print("Você digitou uma entrada inválida")
        self.tempo_digitar = perf_counter() - inicio
