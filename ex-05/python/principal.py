from execstring import ExecString

class Principal():
    """Classe principal para executar o programa"""
    def __init__(self):
        self.strings = ExecString()

    def executar(self):
        self.strings.execute()
