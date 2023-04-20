import json
import pandas as pds
import random
import numpy as np

#script to simulate players and save data

turns = 250
players = 100000

data = pds.read_csv("Monopoly Prices.csv")
board = pds.read_csv("Monopoly Board.csv")

simulated_data = {}
for item in list(data["Name"]):
    simulated_data[item] = np.zeros((1, turns))

for i in range(players):
    print(i)

    turns_played = 0
    position = 0
    doubles_count = 0

    while turns_played < turns-1:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        #Handle doubles
        if dice_1 == dice_2:
            doubles_count += 1
        else:
            turns_played += 1
            doubles_count = 0

        if doubles_count == 3:
            doubles_count = 0
            position = list(board["Name"]).index("In Jail")
            continue

        position += dice_1 + dice_2
        position = position % 40
        landed = list(board["Name"])[position]

        if landed == "To Jail":
            position = list(board["Name"]).index("In Jail")

        elif landed == "Chance":
            rand = random.randint(1, 16)
            match rand:
                case 1:
                    position = list(board["Name"]).index("Boardwalk (DB2)")
                case 2:
                    position = list(board["Name"]).index("Go")
                case 3:
                    position = list(board["Name"]).index("Illinois Avenue (R3)")
                case 4:
                    position = list(board["Name"]).index("St. Charles Place (M1)")
                case 5:
                    #Nearest Railroad
                    if list(board["Name"]).index("Short Line") <= position or position < list(board["Name"]).index("Reading Railroad"):
                        position = list(board["Name"]).index("Reading Railroad")
                    elif list(board["Name"]).index("Reading Railroad") <= position < list(board["Name"]).index("Pennsylvania Railroad"):
                        position = list(board["Name"]).index("Pennsylvania Railroad")
                    elif list(board["Name"]).index("Pennsylvania Railroad") <= position < list(board["Name"]).index("B&O Railroad"):
                        position = list(board["Name"]).index("B&O Railroad")
                    elif list(board["Name"]).index("B&O Railroad") <= position < list(board["Name"]).index("Short Line"):
                        position = list(board["Name"]).index("Short Line")
                    else:
                        raise("If your seeing this message, it means you messed up the nearest railroad match statment. Nice job!")
                                        
                case 6:
                    #Nearest Railroad
                    if list(board["Name"]).index("Short Line") <= position or position < list(board["Name"]).index("Reading Railroad"):
                        position = list(board["Name"]).index("Reading Railroad")
                    elif list(board["Name"]).index("Reading Railroad") <= position < list(board["Name"]).index("Pennsylvania Railroad"):
                        position = list(board["Name"]).index("Pennsylvania Railroad")
                    elif list(board["Name"]).index("Pennsylvania Railroad") <= position < list(board["Name"]).index("B&O Railroad"):
                        position = list(board["Name"]).index("B&O Railroad")
                    elif list(board["Name"]).index("B&O Railroad") <= position < list(board["Name"]).index("Short Line"):
                        position = list(board["Name"]).index("Short Line")
                    else:
                        raise("If your seeing this message, it means you messed up the nearest railroad match statment. Nice job!")
                case 7:
                    #Nearest Utility
                    if list(board["Name"]).index("Water") <= position or position < list(board["Name"]).index("Electric"):
                        position = list(board["Name"]).index("Electric")
                    else:
                        position = list(board["Name"]).index("Water")
                case 8:
                    position = list(board["Name"]).index("In Jail")
                case 9:
                    position = list(board["Name"]).index("Reading Railroad")
                case _:
                    pass
                
        elif landed == "Community Chest":
            rand = random.randint(1, 16)
            match rand:
                case 1:
                    position = list(board["Name"]).index("Go")
                case 2:
                    position = list(board["Name"]).index("To Jail")
                case _:
                    pass
        
        if landed in list(data["Name"]):
            simulated_data[landed][0][turns_played] += 1

for k in simulated_data:
    simulated_data[k] = list(simulated_data[k][0])

with open("data.txt", "w") as p:
    json.dump(simulated_data, p) 