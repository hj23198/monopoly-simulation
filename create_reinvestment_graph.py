import numpy as np
import json
import pandas as pds

from plotfns import *

headers = pds.read_csv("Monopoly Prices.csv")

with open("data.txt", "r") as f:
    data = json.load(f) 

#convert to np
for k in data:
    data[k] = np.array(data[k])

#average data over each player in simulation
data = apply_dict_fuction(data, lambda x: x/100000)

data = combine_by_color(data)

#create arrays for tracking profit
for k in data:
    data[k]["Profit Tracker"] = np.zeros(250)

for k in data:

    housing_list = ["Rent", "Rent (1 House)", "Rent (2 Houses)", "Rent (3 Houses)", "Rent (4 Houses)", "Rent (Hotel)"]
    current_hoursing = dict([[name, 0] for name in data[k] if name != "Profit Tracker"])
    current_money = 0
    total_money = 0 

    for round_num in range(250):

        #add amount earned for each property 
        for money_loop in data[k]:
            if money_loop == "Profit Tracker":
                continue

            landing_chance = data[k][money_loop][round_num]
            table_index = list(headers["Name"]).index(money_loop)
            amount_per_land = list(headers[housing_list[current_hoursing[money_loop]]])[table_index]

            current_money += amount_per_land * landing_chance 
            total_money += amount_per_land * landing_chance 

            data[k]["Profit Tracker"][round_num] = total_money


        #get any property name in color set for obtaining housing price 
        property_name = list(data[k].keys())[0] if list(data[k].keys())[0] != "Profit Tracker" else data[k].values[1]
        
        property_index = list(headers["Name"]).index(property_name)
        housing_price = list(headers["Price per house"])[property_index]

        #spend all money on houses
        if current_money >= housing_price:
            for _ in range(int(current_money // housing_price)):

                keys = list(current_hoursing.keys())
                values = list(current_hoursing.values())

                #ensure 5 houses is not exceeded
                lowest_value = min(values)
                if lowest_value == 5:
                    break

                lowest_index = values.index(lowest_value)
                current_hoursing[keys[lowest_index]] += 1
                current_money -= housing_price


data_new = {}
for _k in data:
    data_new[_k] = data[_k]["Profit Tracker"]
    keys = [k for k in data[_k].keys() if k != "Profit Tracker"]
    total_cost = 0
    for key in keys:
        index = list(headers["Name"]).index(key)
        total_cost += list(headers["Price"])[index]

    data_new[_k] /= total_cost

data = data_new

plot_dict_color(data, "Turn", "ROI", "Investment Model")





        


    
        



