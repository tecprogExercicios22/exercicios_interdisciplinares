class Abreviador():
    """Classe que armazena e abrevia o nome"""
    def __init__(self):
        self.nome = ""
        self.abrev = ""

    def setNome(self):
        self.nome = str(input("Digite seu nome: ")).title()

    def abreviar(self):
        nomes = self.nome.split()
        for nome in nomes:
            if(len(nome) > 2):
                self.abrev += nome[0]
                self.abrev += ". "
            else:
                self.abrev += nome
                self.abrev += " "
        self.abrev = self.abrev.strip()

    def getNome(self):
        return self.nome

    def getAbrev(self):
        return self.abrev
