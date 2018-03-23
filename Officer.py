class Officer:
    def __init__(self, officerID, name, sex, dob):
        self.officerID = officerID
        self.name = name
        self.sex = sex
        self.dob = dob

    def getPrisonerID(self):
        return self.prisonerID

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getDob(self):
        return self.dob