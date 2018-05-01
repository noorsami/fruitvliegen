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
            newMel = copy.copy(mel)
            newMelList.append(helper.swapMel(i,j,newMel))

    return newMelList

def breadthFirst(mel,mir):

    newMel = copy.copy(mel)
    newMelList = [newMel]
    swap = 0

    while mir not in newMelList:
        for i in newMelList:
            swappedList = swapAll(i)
            print("i: ", i)
            time.sleep(0.5)
            for j in swappedList:
                print("j: ", j)
                time.sleep(0.5)
                if j not in newMelList:
                    newMelList.append(j)
                    swap+=1
                    print("newMelList: ",newMelList)

breadthFirst(data.mel,data.mir)
