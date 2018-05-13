import random as rm
import math as m
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper


def breadthFirst(mir,mel):
    mir = tuple(mir)
    melList = [copy.copy(mel)]
    swaps = 0
    melListHistory = [1]

    while mir not in melList:
        swaps+=1
        newMelList = copy.copy(melList)
        for gen in melList:
            swappedList = helper.swapAll(gen)

            for swap in swappedList:
                newMelList.append(swap)

        melList = helper.noDublicates(newMelList)
        melListHistory.append(len(newMelList))
    return melListHistory, swaps

def experimentGraph(length):
    while length > 3:
        for j in range(10):
            title = "BreadthFirst vs Theoretical; N =" + str(length)
            gen1 = [*range(1,length + 1)]
            gen2 = [*range(1,length + 1)]
            rm.shuffle(gen2)
            data = breadthFirst(gen1, gen2)
            swapAmountList = np.zeros(len(data[0]))
            swapAmount = length * (length - 1) / 2

            for i in range(len(swapAmountList)):
                swapAmountList[i] = swapAmount**i
            fig = plt.figure()
            plt.plot(range(data[1] + 1),data[0], label = "breadthFirst")
            plt.plot(range(data[1] + 1), swapAmountList, label = "Theoretical")
            plt.xticks(np.arange(0, data[1]+1, 1))
            plt.xlabel("Number of swaps")
            plt.ylabel("Amount of swap-possibilities")
            plt.title(title)
            plt.legend()
            filename = title + "_#"+ str(j + 1) + ".png"
            fig.savefig(filename, dpi=fig.dpi)

        length-=1

# experiment(9)

def experimentSwapCount():
    length = 8
    histData = []
    for i in range(10**3):
        gen1 = [*range(1,length + 1)]
        gen2 = [*range(1,length + 1)]
        rm.shuffle(gen2)
        histData.append(breadthFirst(gen1,gen2)[1])
    print(histData)
    plt.hist(histData)
    plt.xticks(np.arange(0, length+1, 1))
    plt.show()

# experimentSwapCount()
