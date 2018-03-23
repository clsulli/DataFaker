class Jail:
    def __init__(self, jailID, phone, name, address):
        self.jailID = jailID
        self.phone = phone
        self.name = name
        self.address = address

    def getJailID(self):
        return self.jailID

    def getPhone(self):
        return self.phone

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address