import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
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


fig, ax = plt.subplots(2, 3)

labels = ["Rent", "Rent (1 House)", "Rent (2 Houses)", "Rent (3 Houses)", "Rent (4 Houses)", "Rent (Hotel)"]
plot_data = []
for i in range(6):
    plot_data.append(deepcopy(simulated_data))
    plot_data[i] = combine_by_color(plot_data[i])
    plot_data[i] = colorset_ROI(plot_data[i], data, i)
    plot_data[i] = cumulative_data(plot_data[i])

plot_num = 0
titles = ["Rent", "One House", "Two Houses", "Three Houses", "Four Houses", "Hotel"]

#probably a better way to do this
for x in range(2):
    for y in range(3):
        for k in plot_data[plot_num]:
            match k:
                case "B":
                    ax[x, y].plot(plot_data[plot_num][k], c="brown", label=k)
                case "LB":
                    ax[x, y].plot(plot_data[plot_num][k], c="lightskyblue", label=k)
                case "M":
                    ax[x, y].plot(plot_data[plot_num][k], c="purple", label=k)
                case "O":
                    ax[x, y].plot(plot_data[plot_num][k], c="orange", label=k)
                case "R":
                    ax[x, y].plot(plot_data[plot_num][k], c="red", label=k)
                case "Y":
                    ax[x, y].plot(plot_data[plot_num][k], c="yellow", label=k)
                case "G":
                    ax[x, y].plot(plot_data[plot_num][k], c="darkgreen", label=k)
                case "DB":
                    ax[x, y].plot(plot_data[plot_num][k], c="darkblue", label=k)
                case _:
                    raise Exception("oops")

        ax[x, y].set_title(titles[plot_num])

        plot_num+= 1


for ax in ax.flat:
    ax.set(xlabel='', ylabel='')


fig.show()











             


        




