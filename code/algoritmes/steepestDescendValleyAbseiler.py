import time
import numpy as np
import matplotlib.pyplot as plt

import random as rm
import math as m
import copy
import time
import queue


import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper
from breadthFirst import breadthFirst


def steepestDescendValleyAbseiler(mir,mel):

    '''
        This function tries a breadth first approach to change 2 lists from one to the other using swaps 
            without dupicates, where the lists are turned into a list of lists, called sequences. The algorithm
            then changes and reverses the order of the list of sequences. If the algorithm finds a swap which has
            less sequences in it, the algorithm from then on only searches for swaps which also have that amount of 
            sequences

        arguments: 2 lists, first mir then mel

        returns: A list with the size of each generation, the amount of swaps needed to go from the first list
                to the second and lastly the amount of sequences in each generation
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

    # amount of breakpoints each iteration
    breakpoints = []

    # starting breakpoint
    melLen = len(helper.makeSequence(mel))

    while mir not in melSet:

        melListHistory.append(len(melList))
        breakpoints.append(melLen)

        # put the swaps in the queue
        q.put(copy.copy(melList))

        # clear the swaps of the last generation
        melList = []
        allGens = q.get()
        swaps+=1

        # iterate over all gens
        for gen in allGens:
            seq = helper.makeSequence(gen)
            allSwaps = helper.swapAllSequence(seq)


            for swap in allSwaps:

                # make a new sequence of the swap
                swap = helper.makeSequence(helper.makeList(swap))

                # check if the new sequence is smaller than the last
                # smallest sequence
                if len(swap) <= melLen:
                	melLen = len(swap)
                	swap = helper.makeList(swap)

                    # to avoid duplicates
                	if swap not in melSet:
                		melSet.add(swap)
                		melList.append(swap)

    return melListHistory, swaps, breakpoints
