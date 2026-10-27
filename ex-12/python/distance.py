class Distance():
    def __init__(self):  # 0  1  2  3  4
        self.distances = [[00,15,30,5,12],
                          [15,00,10,17,28],
                          [30,10,00,3,11],
                          [5,17,3,00,80],
                          [12,28,11,80,00]]
        self.traveled = []
        self.absDist = 0

    def setTraveled(self):
        str_input = str(input()).replace(" ", "").split(",")
        self.traveled = [int(x) - 1 for x in str_input]

    def calcDist(self):
        for x in range(0, len(self.traveled) - 1):
            self.absDist += self.distances[self.traveled[x]][self.traveled[x+1]]
    
    def getDist(self) -> int:
        return self.absDist
