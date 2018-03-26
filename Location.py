class Location:
    def __init__(self, district, block, street):
         self.street = street
         self.block = block
         self.district = district

    def getStreet(self):
        return self.street

    def getBlock(self):
        return self.block

    def getDistrict(self):
        return self.district

    def toString(self):
        return "DISTRICT: " + str(self.district) + " BLOCK: " + str(self.block) + " STREET: " + str(self.street)
