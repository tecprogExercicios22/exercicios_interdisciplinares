class Permutador():
    """Avalia se dois valores entrados pelo usuário são permutação um do outro"""
    def __init__(self):
        self.numeros = [0, 0]

    def setNumeros(self):
        i = 0
        while i < 2:
            try:
                valor = int(input("Entre com um dos numeros a serem comparados: "))
                if valor > 0:
                    self.numeros[i] = valor
                    i += 1
                else:
                    print("Erro: O número deve ser estritamente positivo.")
            except ValueError:
                print("Erro: Entrada inválida. Introduza um número inteiro.")

    def getNumeros(self):
        return self.numeros

    def getPermutacoes(self):
        digitos1 = sorted([c for c in str(self.numeros[0]) if c != '0'])
        digitos2 = sorted([c for c in str(self.numeros[1]) if c != '0'])
        
        return digitos1 == digitos2
