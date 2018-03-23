class Crime:
    def __init__(self, caseID, date, domestic, fbiID):
         self.caseID = caseID
         self.date = date
         self.domestic = domestic
         self.fbiID = fbiID

    def getCaseID(self):
        return self.caseID

    def getDate(self):
        return self.date

    def getDomestic(self):
        return self.domestic

    def getFbiID(self):
        return self.fbiID


