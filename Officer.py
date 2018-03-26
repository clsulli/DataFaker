class Officer:
    def __init__(self, officerID, name, sex, dob):
        self.officerID = officerID
        self.name = name
        self.sex = sex
        self.dob = dob

    def getOfficerID(self):
        return self.officerID

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getDob(self):
        return self.dob

    def toString(self):
        return " OFFICERID: " + str(self.officerID) + " NAME: " + str(self.name) + " SEX: " + str(self.sex) + " DOB: " + str(self.dob)