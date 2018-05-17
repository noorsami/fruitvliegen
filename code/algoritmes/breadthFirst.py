import random as rm
import math as m
import copy
import time
import matplotlib.pyplot as plt
import numpy as np
import queue

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper

def breadthFirst(mir,mel):
    '''
        Wat de functie doet.

    Arguments:
        type: wat voor informatie bevat deze var

    Returns:
        type: idem.

    '''
    mir = tuple(mir)
    melSet = set(tuple(copy.copy(mel)))
    melList = [tuple(copy.copy(mel))]
    swaps = 0
    melListHistory = [1]
    count = 0
    q = queue.Queue()
    while mir not in melSet:
        q.put(copy.copy(melList))
        melList = []
        while not q.empty():
            swaps+=1
            allGens = q.get()
            for gen in allGens:
                allSwaps = helper.swapAll(gen)
                for swap in allSwaps:
                    if swap not in melSet:
                        melSet.add(swap)
                        melList.append(swap)
                    else:
                        count += 1

        melListHistory.append(len(melSet))
    return melListHistory, swaps, count



def experimentGraph(length):
    while length > 3:
        for j in range(10):
            title = "BreadthFirst vs Theoretical; N = " + str(length)
            gen1 = [*range(1,length + 1)]
            gen2 = [*range(1,length + 1)]
            rm.shuffle(gen2)
            data = breadthFirst(gen1, gen2)
            swapAmountList = np.zeros(len(data[0]))
            swapAmount = length * (length - 1) / 2
            swapAmountList[0] = 1
            for i in range(1,len(swapAmountList)):
                swapAmountList[i] = (1 + swapAmount)*swapAmountList[i-1]
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

# experimentGraph(9)

def experimentSwapCount(length,amount):
    histData = []
    title = "Histogram of " + str(amount) + " breadthFirst algorithms"
    for i in range(amount):
        gen1 = [*range(1,length + 1)]
        gen2 = [*range(1,length + 1)]
        rm.shuffle(gen2)
        histData.append(breadthFirst(gen1,gen2)[1])

    plt.hist(histData)
    plt.xlabel("Number of swaps")
    plt.ylabel("Amount of solutions")
    plt.title(title)
    plt.xticks(np.arange(0, length+1, 1))
    plt.show()

# experimentSwapCount(5,10)
