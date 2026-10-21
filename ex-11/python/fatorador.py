class Fatorador():
    def __init__(self):
        self.num = 0
        self.fatores = []

    def setNum(self):
        if len(self.fatores) > 0:
            self.fatores.clear()
        self.num = int(input("Entre com o número que deseja fatorar: "))
        if self.num < 2:
            print("Não existe primo menor que 2")
    
    def printFatores(self):
        dividindo = self.num
        for nums in self.fatores:
            print(f"{dividindo} / {nums} = {dividindo//nums}")
            dividindo //= nums

    def prox_primo(self, n) -> int:
        """Método para encontrar o próximo num primo"""
        e_primo = False
        num = n
        while e_primo == False:
            num += 1
            for primo in self.fatores:
                if num % primo == 0:
                    break
            else:
                e_primo = True
                return num
        return 1

    def fatorador(self):
        res_divisao = self.num
        index = -1
        atual_fator = 2
        while res_divisao != 1:
            if len(self.fatores) > 0:
                atual_fator = self.fatores[index]
            while res_divisao % atual_fator != 0:
                atual_fator = self.prox_primo(atual_fator)
            self.fatores.append(atual_fator)
            index += 1
            res_divisao //= self.fatores[index]
