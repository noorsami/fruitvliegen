# alwan
import random as rm
import math as m
import copy
import time

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from datastructuur import data, node, linkedList
from helper import helper

def swapAll(mel):
    newMelList = []
    for i in range(len(mel)):
        for j in range(i):
            newMelList.append(helper.swapped(i,j,mel))

    return newMelList

def noDublicates(list):
    listSet = set(tuple(item) for item in list)
    noDublicate = []
    for item in listSet:
        noDublicate.append(item)
    return noDublicate


def breadthFirst(mir,mel):
    mir = tuple(mir)
    newMel = copy.copy(mel)
    newMelList = [newMel]
    swaps = 0
    melListHistory = [1]
    while mir not in newMelList:
        swaps+=1
        for gen in newMelList:
            swappedList = swapAll(gen)
            for swap in swappedList:
                newMelList.append(swap)
            newMelList = noDublicates(newMelList)
            melListHistory.append(len(newMelList))
    return melListHistory
