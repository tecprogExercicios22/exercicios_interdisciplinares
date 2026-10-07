from criptografia import Criptografado

class Principal():
    def __init__(self):
        self.cript_conteudo = Criptografado(3)

    def executar(self):
        self.cript_conteudo.getConteudo()
        self.cript_conteudo.criptografar()
        self.cript_conteudo.descriptografar()
