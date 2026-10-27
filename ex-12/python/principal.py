from distance import Distance

class Principal():
    def __init__(self):
        self.calc = Distance()
    
    def execute(self):
        print("Insira os locais visitados em ordem:")
        self.calc.setTraveled()
        self.calc.calcDist()
        print(f"A distância total percorrida foi de {self.calc.getDist()} km")
