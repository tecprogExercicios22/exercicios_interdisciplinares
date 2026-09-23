from abreviador import Abreviador

class Principal():
    """Classe principal do script"""
    def __init__(self):
        self.nome = Abreviador()

    def executar(self):
        self.nome.setNome()
        self.nome.abreviar()
        print(f"Nome completo inserido: {self.nome.getNome()}")
        print(f"Abreviação do nome: {self.nome.getAbrev()}")
