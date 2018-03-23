from Crime import *
from Location import *
from Criminal import *
from Officer import *
from Cell import *
from Jail import *
from Block import *
from District import *



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

populateDistrictWithCops(cops)

print(district1.blocks[0].streets)
print(district1.cops[0].officerID)



