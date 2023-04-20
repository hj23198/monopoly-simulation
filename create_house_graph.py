import numpy as np
from copy import deepcopy
import json
import pandas as pds

from plotfns import *

data = pds.read_csv("Monopoly Prices.csv")

with open("data.txt", "r") as p:
    simulated_data = json.load(p) 

#convert to np array 
for k in simulated_data:
    simulated_data[k] = np.array(simulated_data[k])

#average over playercount
simulated_data = apply_dict_fuction(simulated_data, lambda x: x/100000)

labels = ["Rent", "Rent (1 House)", "Rent (2 Houses)", "Rent (3 Houses)", "Rent (4 Houses)", "Rent (Hotel)"]
plot_data = []
for i in range(6):
    plot_data.append(deepcopy(simulated_data))
    plot_data[i] = combine_by_color(plot_data[i])
    plot_data[i] = colorset_ROI(plot_data[i], data, i)
    plot_data[i] = cumulative_data(plot_data[i])

#this is truly the most readable code I've ever written
#replaces over time data with last element 
for i in plot_data:
    for k in i:
        i[k] = i[k][len(i[k])-1]
        
#transforms plot_data into list of house nums
new_data = dict([[key, []] for key in plot_data[0]])

for i in plot_data:
    for k in i:
        new_data[k].append(i[k])

plot_dict_color(new_data, "Amount of houses", "ROI", "ROI based on Amount of Houses")

