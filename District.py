import random
from Location import *

class District:
    def __init__(self, districtNum, blocks, cops):
        self.districtNum = districtNum
        self.blocks = blocks
        self.cops = cops
        self.currBlock = None

    def getRandomBlock(self):
        self.currBlock = random.choice(self.blocks)
        return self.currBlock

    def getRandomOfficer(self):
        arrestingOfficer = random.choice(self.cops)
        return arrestingOfficer

    def getRandomLocation(self):
        block = self.getRandomBlock()
        street = block.getRandomStreet()
        location = Location(self.districtNum, block.blockName, street)
        return location
