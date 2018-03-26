class CrimeOccurence:

    def __init__(self, crime, arrestingOfficer, criminal, location, jail, cell):
        self.crime = crime
        self.arrestingOfficer = arrestingOfficer
        self.criminal = criminal
        self.location = location
        self.jail = jail
        self.cell = cell

    def toString(self):
        print(self.crime.toString() + " " + self.arrestingOfficer.toString() + " " + self.criminal.toString() + " " + self.location.toString() + " " + self.jail.toString() + " " + self.cell.toString())

    def getCaseID(self):
        return str(self.crime.getCaseID())

    def getDate(self):
        return str(self.crime.getDate())

    def getDomestic(self):
        return str(self.crime.getDomestic())

    def getDescription(self):
        return str(self.crime.getDescription())

    def getStreet(self):
        return str(self.location.getStreet())

    def getBlock(self):
        return str(self.location.getBlock())

    def getDistrict(self):
        return str(self.location.getDistrict())

    def getCrimID(self):
        return str(self.criminal.getPrisonerID())

    def getCrimName(self):
        return str(self.criminal.getName())

    def getCrimSex(self):
        return str(self.criminal.getSex())

    def getCrimDob(self):
        return str(self.criminal.getDob())

    def getOfficerID(self):
        return str(self.arrestingOfficer.getOfficerID())

    def getOfficerName(self):
        return str(self.arrestingOfficer.getName())

    def getOfficerSex(self):
        return str(self.arrestingOfficer.getSex())

    def getOfficerDob(self):
        return str(self.arrestingOfficer.getDob())

    def getJailID(self):
        return str(self.jail.getJailID())

    def getJailPhone(self):
        return str(self.jail.getPhone())

    def getJailName(self):
        return str(self.jail.getName())

    def getJailAddress(self):
        return str(self.jail.getAddress())

    def getCellID(self):
        return str(self.cell.getCellID())

    def getCellPriorityLevel(self):
        return str(self.cell.getPriorityLevel())

    def getCellWindow(self):
        return str(self.cell.getWindow())