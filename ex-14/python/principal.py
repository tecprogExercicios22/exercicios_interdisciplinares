from notas import Wnotas, Rnotas

class Principal():
    def __init__(self):
        self.acao = int(input("Digite o valor da ação:\n1 - Escrever\n2 - Ler\n"))

    def executar(self):
        if self.acao == 1:
            escrever = Wnotas('notas.txt')
            for _ in range(0,3):
                dados = []
                print("\n")
                dados.append(str(input("Digite o nome do aluno: ")))
                dados.append(int(input("Digite o RA: ")))
                dados.append(int(input("Digite a nota 1: ")))
                dados.append(int(input("Digite a nota 2: ")))
                escrever.inserir(dados)
        elif self.acao == 2:
            ler = Rnotas('notas.txt')
            ler.lerAlunos()
        else:
            print("Você digitou uma ação inválida")
