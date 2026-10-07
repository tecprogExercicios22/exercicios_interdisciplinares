class Criptografado():
    def __init__(self, chave=1):
        self.k = chave
        self.conteudo = ""

    def getConteudo(self):
        conteudo_temp = str(input("Digite o valor a ser criptografado: ")).lower()
        #metodo necessario para manter apenas letras
        self.conteudo = "".join([c for c in conteudo_temp if c.isalpha() or c == " "])

    def criptografar(self):
        if self.k != 0:
            temp = ""
            for letra in self.conteudo:
                if letra == " ":
                    letra = "{"
                letra = chr(((ord(letra) - 97 + self.k) % 27) + 97)
                if(letra == "{"):
                   letra = " "
                temp += letra
            self.conteudo = temp
        print(self.conteudo)

    def descriptografar(self):
        if self.k != 0:
            temp = ""
            for letra in self.conteudo:
                if letra == " ":
                   letra = "{"
                letra = chr(((ord(letra) - 97 - self.k) % 27) + 97)
                if letra == "{":
                    letra = " "
                temp += letra
            self.conteudo = temp
        print(self.conteudo)
