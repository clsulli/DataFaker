import random
import time

class Crime:
    def __init__(self, caseID):
         self.caseID = caseID
         self.date = None
         self.domestic = False
         self.crimeTypes = ['Arson', 'Assault', 'Blackmail', 'Bribery', 'Burglary', 'Embezzlement', 'Extortion', 'False pretenses',
                            'Larceny', 'Pickpocketing', 'Stealing', 'Robbery', 'Smuggling', 'Tax Evasion', 'Theft', 'Murder']
         self.crimeType = None

    def getCaseID(self):
        return self.caseID

    def getDate(self):
        return self.date

    def getDomestic(self):
        return self.domestic

    def getFbiID(self):
        return self.fbiID

    def getDescription(self):
        return self.crimeType

    def getCrimeType(self):
        self.crimeType = random.choice(self.crimeTypes)
        choices = [True, False]
        if self.crimeType == 'Assault':
            choice = random.choice(choices)
            self.domestic = choice

        def strTimeProp(start, end, format, prop):
            """Get a time at a proportion of a range of two formatted times.

            start and end should be strings specifying times formated in the
            given format (strftime-style), giving an interval [start, end].
            prop specifies how a proportion of the interval to be taken after
            start.  The returned time will be in the specified format.
            """

            stime = time.mktime(time.strptime(start, format))
            etime = time.mktime(time.strptime(end, format))

            ptime = stime + prop * (etime - stime)

            return time.strftime(format, time.localtime(ptime))

        def randomDate(start, end, prop):
            return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

        self.date = randomDate("1/1/2017 12:00 AM", "12/31/2017 11:59 PM", random.random())


    def toString(self):
        return "CASE ID: " + str(self.caseID) + " DATE: " + str(self.date) + " DOMESTIC: " + str(self.domestic) + " CRIME: " + str(self.crimeType)


