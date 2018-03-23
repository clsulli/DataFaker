class Location:
    def __init__(self, street, block, district):
         self.street = street
         self.block = block
         self.district = district

    def getStreet(self):
        return self.street

    def getBlock(self):
        return self.block

    def getDistrict(self):
        return self.district
