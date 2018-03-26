from Crime import *
from Location import *
from Criminal import *
from Officer import *
from Cell import *
from Jail import *
from Block import *
from District import *
from CrimeOccurrence import *
from faker import Faker
import time
import random
import mysql.connector

def importStreets(filename):
    streets = []

    fileO = open(filename, "r")
    streetsF = fileO.readlines()

    for street in streetsF:
        streets.append(street.strip('\n'))

    return streets

def importCops(filename):
    cops = []

    fileO = open(filename, "r")
    copsF = fileO.readlines()

    for cop in copsF:
        copLine = cop.split(',')
        copID, copName, copGender, copDob = copLine[0], copLine[1], copLine[2], copLine[3]
        currCop = Officer(copID, copName, copGender, copDob)
        cops.append(currCop)

    return cops

def populateDistrictsWithStreets(streets, dis, blocks, startIdx):
    blocksO = []

    blockStreets1 = []
    blockStreets2 = []
    blockStreets3 = []
    blockStreets4 = []
    blockStreets5 = []

    for street in range(startIdx, startIdx + 39):
        blockStreets1.append(streets[street])

    blocksO.append(Block(blocks[0], blockStreets1))

    for street in range(startIdx + 40, startIdx + 79):
        blockStreets2.append(streets[street])

    blocksO.append(Block(blocks[1], blockStreets2))

    for street in range(startIdx + 80, startIdx + 119):
        blockStreets3.append(streets[street])

    blocksO.append(Block(blocks[2], blockStreets3))

    for street in range(startIdx + 120, startIdx + 159):
        blockStreets4.append(streets[street])

    blocksO.append(Block(blocks[3], blockStreets4))

    for street in range(startIdx + 160, startIdx + 199):
        blockStreets5.append(streets[street])

    blocksO.append(Block(blocks[4], blockStreets5))

    return District(dis, blocksO, [])

def populateDistrictWithCops(cops):

    for cop in range(0, len(cops)):
        if cop >= 0 and cop <= 499:
            district1.cops.append(cops[cop])
        elif cop >= 500 and cop <= 999:
            district2.cops.append(cops[cop])
        elif cop >= 1000 and cop <= 1499:
            district3.cops.append(cops[cop])
        elif cop >= 1500 and cop <= 1999:
            district4.cops.append(cops[cop])
        elif cop >= 2000 and cop <= 2499:
            district5.cops.append(cops[cop])

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

def generateJails():
    jails = []

    jail1 = Jail(1, "555-3459-1527", "Alkatraz", "401 New Castle Crossing")
    jail2 = Jail(2, "555-1853-2850", "Guantanomo", "578 Lillian Parkway")

    jails.append(jail1)
    jails.append(jail2)

    return jails

def populateCriminals():
    criminalList = []
    faker = Faker()
    sexs = ["Male", "Female"]

    for i in range(0,200000):
        name = faker.name()
        sex = random.choice(sexs)
        dob = randomDate("1/1/1970 12:00 AM", "12/31/2002 11:59 PM", random.random())
        criminalList.append(Criminal(i, name, sex, dob))

    return criminalList

def generateCrime(districts, criminals, jails):
    crimes = []
    cells = []
    priorityLevels = ['Low', 'Medium', 'High', 'Severe']
    windows = ["Y", "N"]

    for i in range(0, 100000):
        cells.append(i)

    for i in range(0, 200000):
        currCrime = Crime(i)
        currCrime.getCrimeType()
        district = random.choice(districts)
        jail = random.choice(jails)
        priorityLevel = random.choice(priorityLevels)
        window = random.choice(windows)
        cell = Cell(random.choice(cells), jail.jailID, priorityLevel, window)

        crimeOcc = CrimeOccurence(currCrime, district.getRandomOfficer(), criminals[i], district.getRandomLocation(), jail, cell)
        crimes.append(crimeOcc)

        crimeOcc.toString()

    return crimes

def generateSQLStatementsForCrime(crimes):
    crimesO = crimes
    sqlWriter = open("SQL-Commands.txt", "w")

    def insertCrime(caseID, date, domestic, description):
        return 'insert into crime (date, domestic, description, id) values (' + '"' + date + '"' + ',' + '"' + domestic + '"' + ',' + '"' + description + '"' + ',' + caseID + ');'

    def insertLocation(caseID, street, block, district):
        return 'insert into location (locationAPI, block, district, id) values ( "' + street + '" , "' + block + '" , "' + district + '" ,' + caseID + ' );'

    def insertCriminal(caseID, prisonerID, name, sex, dob):
        return 'insert into criminal (prisonerID, name, sex, dob, id) values (' + prisonerID + ', "' + name + '" , "' + sex + '" , "' + dob + '" ,' + caseID + ');'

    def insertArrestingOfficer(caseID, officerID, name, sex, dob):
        return 'insert into arresting_officer (officerID, name, sex, dob, id) values (' + officerID + ', "' + name + '" , "' + sex + '" , "' + dob.strip('\n') + '" ,' + caseID + ');'

    def insertJail(caseID, jailID, phone, name, address):
        return 'insert into jail (jailID, phone, name, address, id) values (' + jailID + ', "' + phone + '" , "' + name + '" , "' + address + '" ,' + caseID + ');'

    def insertCell(caseID, cellID, jailID, priorityLevel, window):
        return 'insert into cell (cellID, jailID, priorityLevel, window, id) values (' + cellID + ',' + jailID + ', "' + priorityLevel + '" , "' + window + '" ,' + caseID + ');'

    def insertOccurred(caseID, street):
        return 'insert into occurred (locationAPI, id) values ( "' + street + '" , ' + caseID + ');'

    def insertContatains(caseID, officerID, prisonerID):
        return 'insert into contains (officerID, prisonerID, id) values ( ' + officerID + ',' + prisonerID + ',' + caseID + ');'

    def insertArrestedBy(caseID, officerID, prisonerID):
        return 'insert into arrested_by (officerID, prisonerID, id) values (' + officerID + ',' + prisonerID + ',' + caseID + ');'

    def insertOccupies(caseID, prisonerID, jailID, cellID):
        return 'insert into occupies (prisonerID, jailID, cellID, id) values (' + prisonerID + ',' + jailID + ',' + cellID + ',' + caseID + ');'

    for i in range(len(crimesO)):

        insCrime = insertCrime(crimesO[i].getCaseID(), crimesO[i].getDate(), crimesO[i].getDomestic(), crimesO[i].getDescription())
        insLocation = insertLocation(crimesO[i].getCaseID(), crimesO[i].getStreet(), crimesO[i].getBlock(), crimesO[i].getDistrict())
        insCriminal = insertCriminal(crimesO[i].getCaseID(), crimesO[i].getCrimID(), crimesO[i].getCrimName(), crimesO[i].getCrimSex(), crimesO[i].getCrimDob())
        insArrestingOfficer = insertArrestingOfficer(crimesO[i].getCaseID(), crimesO[i].getOfficerID(), crimesO[i].getOfficerName(), crimesO[i].getOfficerSex(), crimesO[i].getOfficerDob())
        insJail = insertJail(crimesO[i].getCaseID(), crimesO[i].getJailID(), crimesO[i].getJailPhone(), crimesO[i].getJailName(), crimesO[i].getJailAddress())
        insCell = insertCell(crimesO[i].getCaseID(), crimesO[i].getCellID(), crimesO[i].getJailID(), crimesO[i].getCellPriorityLevel(), crimesO[i].getCellWindow())
        insOccurred = insertOccurred(crimesO[i].getCaseID(), crimesO[i].getStreet())
        insContains = insertContatains(crimesO[i].getCaseID(), crimesO[i].getOfficerID(), crimesO[i].getCrimID())
        insArrestedBy = insertArrestedBy(crimesO[i].getCaseID(), crimesO[i].getOfficerID(), crimesO[i].getCrimID())
        insOccupies = insertOccupies(crimesO[i].getCaseID(), crimesO[i].getCrimID(), crimesO[i].getJailID(), crimesO[i].getCellID())

        sqlWriter.write(insCrime + '\n')
        sqlWriter.write(insLocation + '\n')
        sqlWriter.write(insCriminal + '\n')
        sqlWriter.write(insArrestingOfficer + '\n')
        sqlWriter.write(insJail + '\n')
        sqlWriter.write(insCell + '\n')
        sqlWriter.write(insOccurred + '\n')
        sqlWriter.write(insContains + '\n')
        sqlWriter.write(insArrestedBy + '\n')
        sqlWriter.write(insOccupies + '\n')

district1Blocks = ['O-Block','Brick City','Lamron','Lowe','Doggpound']
district2Blocks = ['Ada Park','1017','WWDC','ABK','GME']
district3Blocks = ['757','CBlock','Folly','CMB','Mac Creek']
district4Blocks = ['Pocket','LPC','Sirconn','LOC','Gutta']
district5Blocks = ['Deathrow','Pax','Low','MTG','KTS']

streets = importStreets("Streets.csv")
cops = importCops("Cops.csv")

district1 = populateDistrictsWithStreets(streets, 1, district1Blocks, 0)
district2 = populateDistrictsWithStreets(streets, 2, district2Blocks, 200)
district3 = populateDistrictsWithStreets(streets, 3, district3Blocks, 400)
district4 = populateDistrictsWithStreets(streets, 4, district4Blocks, 600)
district5 = populateDistrictsWithStreets(streets, 5, district5Blocks, 800)

districts = [district1, district2, district3, district4, district5]

populateDistrictWithCops(cops)
criminals = populateCriminals()
jails = generateJails()

crimes = generateCrime(districts, criminals, jails)

generateSQLStatementsForCrime(crimes)




