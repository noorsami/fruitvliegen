import copy
import queue

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper

def breadthFirst(mir,mel):
    '''
<<<<<<< HEAD
        
=======
        This function tries a breadth first approach to change 2 lists from one to the other using swaps 
            without dupicates

        arguments: 2 lists, first mir then mel
>>>>>>> 330cb844fba62ab1c39e3be6ec15f83891350681

        returns: A list with the size of each generation and the amount of swaps needed to go from the first list
                to the second
    '''

    # make variable useable
    mir = tuple(mir)

    # copy to avoid pointer conflicts
    melSet = set(tuple(copy.copy(mel)))
    melList = [tuple(copy.copy(mel))]
    swaps = 0

    # amount of swaps each iteration
    melListHistory = []
    q = queue.Queue()

    while mir not in melSet:

        melListHistory.append(len(melSet))

        # put everything in the queue and clear the previous generation
        q.put(copy.copy(melList))
        melList = []
        swaps+=1
        allGens = q.get()

        # iterate over all gens

        for gen in allGens:

            allSwaps = helper.swapAll(gen)
            for swap in allSwaps:

                # to avoid duplicates
                if swap not in melSet:
                    melSet.add(swap)
                    melList.append(swap)

        
    return melListHistory, swaps
<<<<<<< HEAD
=======


>>>>>>> 330cb844fba62ab1c39e3be6ec15f83891350681
