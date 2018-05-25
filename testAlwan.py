import time
import matplotlib.pyplot as plt
import numpy as np

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






# def branchAndBound(depth, mir, mel):

#     treeHistory = [helper.makeSequence(tuple(mel))]
#     mir = [tuple(mir)]
#     succes = []
#     print(mel)
#     henk = goingDeep(succes, depth, treeHistory, mir)
#     print(henk)
#     for i in henk:
#         print(i)
#     return henk


def branchAndBound(solutions, bound, mir, mel):
    stack = []
    mir = [tuple(mir)]
    randSeq = helper.makeSequence(tuple(mel))
    stack.append([randSeq])
    history = []

    while stack and solutions:
        current = stack.pop()

        if len(current) < bound:
            allSwaps = helper.swapAllSequence(current[-1])

            for swap in allSwaps:
                swap = helper.makeSequence(helper.makeList(swap))
                # print(swap)
                # print(mir)
                if swap == mir:
                    history.append(current + [swap])
                    bound = len(current)
                    solutions -= 1



                stack.append(current + [swap])
    return history

def makeScore(scoreList):
    score0 = []
    score1 = []
    score2 = []

    for score in scoreList:

        if score[0] == 2:
            score2.append(score[1])
        elif score[0] == 1:
            score1.append(score[1])
        else:
            score0.append(score[1])

    return score2 + score1 + score0


length = 8
gen1 = [*range(1,length + 1)]
gen2 = [*range(1,length + 1)]
rm.shuffle(gen2)
mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for i in branchAndBound(3,14,gen1,gen2):
    print(i)







# data1  = [1, 235, 8784, 2740, 39997, 57155, 42241, 343473, 27862, 79871, 153052, 21481,5740, 9899, 3169, 1851, 525]
# data2 = [22, 22, 21, 19, 18, 16, 15, 14, 12, 11, 10, 8, 7, 6, 5, 4, 3]
# length = 25
# fig = plt.figure()
# title = "steepestAscend; N = " + str(length)
# plt.subplot(211)
# plt.plot(range(len(data1)),data1, label = "Sequences")
# plt.xticks(np.arange(0, len(data1), 1))
# plt.xlabel("Number of swaps")
# plt.ylabel("Number of tried Sequences")
# plt.title(title)
# plt.subplot(212)
# plt.plot(range(len(data2)),data2, label = "Sequences")
# plt.xticks(np.arange(0, len(data2), 1))
# plt.xlabel("Number of swaps")
# plt.ylabel("Lengeth of smallest sequence")
# plt.show()