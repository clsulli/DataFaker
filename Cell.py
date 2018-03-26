class Cell:
    def __init__(self, cellID, jailID, priorityLevel, window):
        self.cellID = cellID
        self.jailID = jailID
        self.priorityLevel = priorityLevel
        self.window = window

    def getCellID(self):
        return self.cellID

    def getJailID(self):
        return self.jailID

    def getPriorityLevel(self):
        return self.priorityLevel

    def getWindow(self):
        return self.window

    def toString(self):
        return "CELLID: " + str(self.cellID) + "JAILID: " + str(self.jailID) + " LEVEL: " + str(self.priorityLevel) + " WINDOW: " + str(self.window)