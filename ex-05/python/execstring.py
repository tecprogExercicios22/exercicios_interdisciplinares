class ExecString():
    def __init__(self):
        self.strings = ["", ""]
        self.reps = 0

    def getStrings(self):
        self.strings[0] = str(input("Insira a primeira string: "))
        self.strings[1] = str(input("Insira a segunda string: "))

    def countStrings(self):
        self.reps = self.strings[0].lower().count(self.strings[1].lower())
        print(f"A string 2 se repete {self.reps} vez(es) dentro da string 1")

    def stats(self):
        for item, texto in enumerate(self.strings):
            texto = texto.lower().replace(" ", "").replace(",", "")
            contagem = {}
            for caractere in texto:
                contagem[caractere] = contagem.get(caractere, 0) + 1
            contagem = dict(sorted(contagem.items()))
            print(f"A string {item + 1} possui tais caracteres e suas repetições:")
            for chave, valor in contagem.items():
                print(f"\t{chave}: {'*'*valor} {valor}")
                

    def execute(self):
        self.getStrings()
        self.countStrings()
        self.stats()
