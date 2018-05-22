
import random as rm
import math as m
import copy
import time
import queue
import matplotlib.pyplot as plt
import numpy as np


import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper
from breadthFirst import breadthFirst

def breadthFirstWithSequences(mir,mel):
    mir = tuple(mir)
    melSet = set(tuple(copy.copy(mel)))
    melList = [tuple(copy.copy(mel))]
    swaps = 0
    melListHistory = []
    q = queue.Queue()
    breakpoints = []

    while mir not in melSet:
        melListHistory.append(len(melList))
        q.put(copy.copy(melList))
        melList = []
        while not q.empty():
            allGens = q.get()
            swaps+=1
            for gen in allGens:
                seq = helper.makeSequence(gen)
                allSwaps = helper.swapAllSequence(seq)

                for swap in allSwaps:
                    swap = helper.makeList(swap)
                    if swap not in melSet:
                        melSet.add(swap)
                        melList.append(swap)

        

    return melListHistory, swaps

def experimentGraph(length):
    while length > 3:
        for j in range(10):
            title = "BreadthFirst vs Sequences; N = " + str(length)
            gen1 = [*range(1,length + 1)]
            gen2 = [*range(1,length + 1)]
            rm.shuffle(gen2)
            data1 = breadthFirst(gen1, gen2)
            data2 = breadthFirstWithSequences(gen1,gen2)
            fig = plt.figure()
            plt.plot(range(data1[1]),data1[0], label = "breadthFirst")
            plt.plot(range(data2[1]), data2[0], label = "Sequences")
            plt.xticks(np.arange(0, data1[1], 1))
            plt.xlabel("Number of swaps")
            plt.ylabel("Number of tried swaps")
            plt.title(title)
            plt.legend()
            filename = title + "_#"+ str(j + 1) + ".png"
            fig.savefig(filename, dpi=fig.dpi)

        length-=1

length =15
experimentGraph(9)
# gen1 = [*range(1,length + 1)]
# gen2 = [*range(1,length + 1)]
# rm.shuffle(gen2)
# mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
# mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# print(breadthFirstWithSequences(gen1,gen2))
