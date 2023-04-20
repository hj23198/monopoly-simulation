import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import re


def cumulative_data(dataset):
    """makes data cumulative"""
    for k in dataset:
        dataset[k] = np.cumsum(dataset[k])
    return dataset

def apply_dict_fuction(dataset, fun):
    """applies function to each datapoint"""
    for k in dataset:
        for i in range(len(dataset[k])):
            dataset[k][i] = fun(dataset[k][i])
    return dataset

def plot_dict_color(dataset, xlabel, ylabel, title):
    """plots dictionary in color"""
    for k in dataset:
        match k:
            case "B":
                plt.plot(dataset[k], c="brown", label=k)
            case "LB":
                plt.plot(dataset[k], c="lightskyblue", label=k)
            case "M":
                plt.plot(dataset[k], c="purple", label=k)
            case "O":
                plt.plot(dataset[k], c="orange", label=k)
            case "R":
                plt.plot(dataset[k], c="red", label=k)
            case "Y":
                plt.plot(dataset[k], c="yellow", label=k)
            case "G":
                plt.plot(dataset[k], c="darkgreen", label=k)
            case "DB":
                plt.plot(dataset[k], c="darkblue", label=k)
            case _:
                raise Exception("color not found")

    plt.legend()
    plt.xlabel(xlabel)
    plt.title(title)
    plt.ylabel(ylabel)


def combine_by_color(dataset):
    """combines property dict into color dict using"""
    dataset_new = {}

    for k in dataset:
        output = re.findall("\(.+\)", k)
        output = output[0][1:output[0].__len__()-1]
        if output.__len__() == 3:
            output = output[0:2]
        else:
            output = output[0:1]

        if output not in dataset_new.keys():
            dataset_new[output] = {}

        dataset_new[output][k] = dataset[k]

    return dataset_new


def colorset_ROI(dataset, headers, amount_house):
    """converts each color into averaged ROI"""
    labels = ["Rent", "Rent (1 House)", "Rent (2 Houses)", "Rent (3 Houses)", "Rent (4 Houses)", "Rent (Hotel)"]
    return_dataset = {}

    for k in dataset:
        return_dataset[k] = np.zeros(250)
        amount = 0
        for c in dataset[k]:

            index = list(headers["Name"]).index(c)
            price = list(headers["Price"])[index]
            price_per_house = list(headers["Price per house"])[index]
            land_price = list(headers[labels[amount_house]])[index]

            return_dataset[k] += dataset[k][c] * land_price
            amount += price_per_house * amount_house + price

        return_dataset[k] = return_dataset[k] / amount

    return return_dataset
        
    




