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


def branchAndBound(depth, mir, mel):

    treeHistory = [0,helper.makeSequence(tuple(mel))]
    i = 0
    mir = [tuple(mir)]
    succes = []
    henk = goingDeep(succes, depth, treeHistory, i, mir)
    return henk


def goingDeep(succes, depth, treeHistory, i, mir):


    try:
        if treeHistory[-1][1] == mir:
            succes.append(treeHistory)
            if len(treeHistory[:-2][1]) is 1:
                goingDeep(succes, len(treeHistory), [treeHistory[:-2]], treeHistory[-2][0] + 1, mir)
            else:
                goingDeep(succes, len(treeHistory), [treeHistory[:-1]], treeHistory[-2][0] + 1, mir)


    except TypeError:
        if treeHistory[-1] == mir:
            goingDeep(succes, len(treeHistory), [treeHistory[:-1]], treeHistory[-2][0] + 1, mir)

    try:
        melSeq = treeHistory[-1]
        breakpoint = len(melSeq)
        allSwaps = helper.swapAllSequence(melSeq)

    except TypeError:

        melSeq = treeHistory[-1][1]
        breakpoint = len(melSeq)
        allSwaps = helper.swapAllSequence(melSeq)

    if len(treeHistory) - 1 + breakpoint / 2 > depth:
        goingDeep(succes, depth, treeHistory[:-1], treeHistory[:-1][0] + 1, mir)

    
    scoreList = []
    score0 = []
    score1 = []
    score2 = []
    for swap in allSwaps:
        swap = helper.makeSequence(helper.makeList(swap))
        scoreList.append([breakpoint - len(swap), swap])

    for score in scoreList:
        if score[0] is 2:
            score2.append(score)
        elif score[0] is 1:
            score1.append(score)
        else:
            score0.append(score)

    allScore = score2 + score1 + score0
    print("allScore: ", allScore)
    print("i: ", i)
    treeHistory.append([i, allScore[i][1]])
    goingDeep(succes, depth, treeHistory, i, mir)

length = 5
gen1 = [*range(1,length + 1)]
gen2 = [*range(1,length + 1)]
rm.shuffle(gen2)
# mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
# mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
branchAndBound(5,gen1,gen2)
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