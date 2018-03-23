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

    return District(dis, blocksO, 5)

district1Blocks = ['O-Block','Brick City','Lamron','Lowe','Doggpound']
district2Blocks = ['Ada Park','1017','WWDC','ABK','GME']
district3Blocks = ['757','CBlock','Folly','CMB','Mac Creek']
district4Blocks = ['Pocket','LPC','Sirconn','LOC','Gutta']
district5Blocks = ['Deathrow','Pax','Low','MTG','KTS']

streets = importStreets("Streets.csv")

district1 = populateDistrictsWithStreets(streets, 1, district1Blocks, 0)
district2 = populateDistrictsWithStreets(streets, 2, district1Blocks, 200)
district3 = populateDistrictsWithStreets(streets, 3, district1Blocks, 400)
district4 = populateDistrictsWithStreets(streets, 4, district1Blocks, 600)
district5 = populateDistrictsWithStreets(streets, 5, district1Blocks, 800)

print(district1.blocks[0].streets)
print(district1.blocks[1].streets)
print(district1.blocks[2].streets)
print(district1.blocks[3].streets)
print(district1.blocks[4].streets)
print("")
print(district2.blocks[0].streets)
print(district2.blocks[1].streets)
print(district2.blocks[2].streets)
print(district2.blocks[3].streets)
print(district2.blocks[4].streets)


