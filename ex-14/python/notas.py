class Wnotas():
    def __init__(self, arquivo):
        self.arquivo = arquivo
        with open(arquivo, 'w', encoding="utf-8") as arquivo:
            pass

    def inserir(self, dados):
        with open(self.arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{len(dados[0])},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")

class Rnotas():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def lerAlunos(self):
        with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                media = (int(dados[3]) + int(dados[4]))/2
                if media < 5:
                    print(f"O aluno {dados[1]}, RA: {dados[2]}, está reprovado com nota {media}")
                elif media < 6:
                    print(f"O aluno {dados[1]}, RA: {dados[2]} e média: {media}, está elegível a fazer recuperação")
                else:
                    print(f"O aluno {dados[1]}, RA: {dados[2]}, está aprovado com nota {media}")
