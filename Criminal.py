class Criminal:
    def __init__(self, prisonerID, name, sex, dob):
        self.prisonerID = prisonerID
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