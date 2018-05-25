
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

    '''
        This function tries a breadth first approach to change 2 lists from one to the other using swaps
            without dupicates, where the lists are turned into a list of lists, called sequences. The algorithm
            then changes and reverses the order of the list of sequences

        arguments: 2 lists, first mir then mel

        returns: A list with the size of each generation and the amount of swaps needed to go from the first list
                to the second
    '''


    # make variables useable
    mir = tuple(mir)

    # copy to avoid pointer conflicts
    melSet = set(tuple(copy.copy(mel)))
    melList = [tuple(copy.copy(mel))]
    swaps = 0

    # amount of swaps each iteration
    melListHistory = []
    q = queue.Queue()

    while mir not in melSet:

        melListHistory.append(len(melList))

        # put the swaps in the queue
        q.put(copy.copy(melList))

        # clear the swaps of the last generation
        melList = []
        allGens = q.get()
        swaps+=1

        for gen in allGens:
            seq = helper.makeSequence(gen)
            allSwaps = helper.swapAllSequence(seq)

            for swap in allSwaps:

                # make a list of the swap in order to add it to the set
                swap = helper.makeList(swap)

                # to avoid duplicates
                if swap not in melSet:
                    melSet.add(swap)
                    melList.append(swap)

    return melListHistory, swaps
