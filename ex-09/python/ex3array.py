class Ex3Array():
    def __init__(self, tam):
        self.tam_maximo = tam
        self.array = []
        self.tam = 0

    def adicionar(self, n):
        if self.tam_maximo >= self.tam:
            try:
                self.array.append(n)
                self.tam += 1
                return True

            except:
                return False

    def calculaMedia(self):
        return sum(self.array)/len(self.array)

    def getTam(self):
        return self.tam_maximo

class Ex3ArrayControle():
    def __init__(self):
        n = int(input("Qual o tamanho do vetor? "))
        self.vetor = Ex3Array(n)
        
    def adicionarNums(self):
        for i in range(0, self.vetor.getTam()):
            self.vetor.adicionar(int(input(f"Informe o número {i + 1} do vetor: ")))

    def getMedia(self):
        print(f"A média dos valores é de: {self.vetor.calculaMedia()}")
