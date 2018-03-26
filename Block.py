import random

class Block:
    def __init__(self, blockName, streets):
        self.blockName = blockName
        self.streets = streets
        self.currStreet = None

    def getRandomStreet(self):
        self.currStreet = random.choice(self.streets)
        return self.currStreet




