# alwan
import random as rm
import math as m
import copy
import time
import queue
#[4, 3, 4, 4, 3, 5, 5, 3, 5, 4, 5, 4, 4, 5, 4, 4, 3, 5, 5, 4, 5, 5, 4, 4, 4, 4, 3                                                                                                                , 5, 4, 6, 4, 4, 5, 5, 2, 4, 3, 3, 3, 3, 5, 5, 5, 4, 3, 4, 5, 5, 5, 3, 4, 5, 4,                                                                                                                 5, 4, 4, 4, 5, 5, 4, 3, 4, 5, 4, 5, 4, 6, 3, 5, 6, 5, 3, 4, 5, 3, 4, 4, 5, 5, 4,                                                                                                                 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 5, 5, 4, 4, 5, 2, 6, 5, 4, 5, 4                                                                                                                , 3, 5, 4, 4, 5, 4, 4, 4, 5, 3, 4, 3, 5, 4, 3, 5, 5, 1, 4, 5, 6, 3, 4, 5, 5, 5,                                                                                                                 5, 4, 4, 3, 5, 4, 3, 4, 4, 4, 4, 4, 3, 4, 3, 4, 4, 5, 4, 4, 5, 5, 4, 5, 4, 5, 5,                                                                                                                 6, 6, 4, 4, 5, 4, 5, 5, 4, 5, 3, 5, 4, 4, 3, 5, 5, 5, 4, 4, 4, 4, 3, 4, 4, 4, 5                                                                                                                , 3, 5, 5, 4, 4, 6, 5, 3, 5, 4, 6, 3, 4, 5, 4, 3, 6, 4, 4, 4, 5, 5, 4, 5, 5, 3,                                                                                                                 4, 4, 5, 4, 4, 4, 4, 4, 5, 3, 5, 3, 4, 5, 4, 5, 5, 4, 4, 5, 3, 3, 5, 4, 5, 3, 4,                                                                                                                 4, 5, 4, 4, 4, 3, 4, 5, 4, 5, 4, 5, 4, 4, 3, 6, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 5                                                                                                                , 2, 5, 5, 3, 5, 4, 4, 5, 5, 4, 6, 4, 4, 4, 5, 5, 5, 6, 5, 5, 5, 4, 4, 5, 3, 4,                                                                                                                 5, 5, 5, 4, 3, 5, 5, 5, 3, 4, 4, 4, 5, 4, 4, 3, 4, 3, 5, 6, 4, 5, 4, 4, 4, 4, 5,                                                                                                                 4, 3, 4, 5, 4, 4, 5, 5, 4, 5, 3, 5, 5, 4, 4, 5, 5, 4, 4, 5, 5, 4, 4, 5, 5, 3, 5                                                                                                                , 4, 6, 4, 4, 5, 5, 4, 3, 4, 5, 5, 3, 5, 3, 4, 5, 4, 5, 5, 5, 4, 5, 5, 3, 4, 5,                                                                                                                 4, 4, 5, 4, 3, 5, 5, 4, 4, 5, 5, 3, 5, 5, 6, 5, 5, 3, 3, 4, 5, 5, 4, 3, 5, 4, 5,                                                                                                                 3, 4, 5, 4, 5, 4, 3, 5, 5, 4, 4, 5, 3, 6, 6, 4, 4, 4, 3, 5, 5, 5, 3, 4, 5, 5, 5                                                                                                                , 4, 5, 3, 4, 4, 5, 5, 5, 4, 5, 3, 5, 4, 5, 4, 4, 4, 4, 3, 4, 3, 5, 3, 6, 4, 4,                                                                                                                 4, 4, 4, 5, 4, 5, 4, 4, 5, 5, 5, 4, 5, 4, 6, 4, 5, 6, 4, 4, 5, 4, 5, 5, 6, 3, 5,                                                                                                                 3, 4, 4, 5, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 5, 3, 5, 5, 4, 4, 5, 5, 5, 5, 5, 5, 4                                                                                                                , 4, 5, 6, 2, 4, 4, 4, 5, 5, 5, 2, 5, 5, 5, 5, 4, 4, 5, 4, 5, 3, 4, 5, 5, 3, 4,                                                                                                                 3, 3, 5, 4, 5, 5, 5, 5, 6, 4, 5, 5, 5, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 2, 4, 4,                                                                                                                 3, 3, 5, 5, 4, 4, 3, 4, 3, 5, 4, 4, 4, 5, 5, 4, 4, 5, 6, 4, 4, 4, 4, 4, 5, 5, 5                                                                                                                , 5, 4, 5, 4, 3, 5, 4, 5, 4, 4, 3, 5, 3, 3, 5, 3, 5, 4, 6, 5, 3, 4, 5, 4, 5, 4,                                                                                                                 5, 5, 2, 5, 5, 4, 5, 4, 5, 2, 5, 5, 5, 4, 5, 6, 5, 4, 3, 3, 4, 4, 5, 5, 4, 4, 3,                                                                                                                 4, 5, 5, 4, 5, 4, 5, 4, 4, 4, 4, 3, 3, 4, 5, 5, 5, 3, 4, 4, 4, 5, 5, 6, 3, 5, 6                                                                                                                , 5, 5, 5, 5, 5, 4, 5, 4, 6, 5, 4, 4, 5, 3, 3, 5, 6, 5, 5, 4, 5, 4, 4, 4, 5, 3,                                                                                                                 6, 5, 4, 4, 4, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 4, 4, 4, 5, 4, 4, 6, 5, 5, 4, 4,                                                                                                                 5, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 5, 3, 5, 4, 4, 4, 6, 5, 5, 5, 5, 5, 4, 4, 4                                                                                                                , 4, 5, 4, 4, 4, 3, 4, 5, 4, 4, 4, 6, 4, 4, 5, 5, 6, 4, 4, 4, 4, 4, 3, 5, 4, 3,                                                                                                                 5, 4, 5, 5, 4, 3, 4, 3, 4, 4, 5, 6, 6, 4, 5, 4, 3, 5, 5, 4, 4, 5, 4, 3, 4, 4, 5,                                                                                                                 5, 5, 5, 5, 5, 4, 5, 5, 4, 3, 3, 5, 3, 3, 6, 4, 4, 3, 3, 5, 3, 6, 4, 4, 5, 5, 4                                                                                                                , 6, 3, 5, 5, 4, 4, 3, 5, 4, 5, 5, 5, 4, 5, 4, 6, 5, 4, 5, 4, 4, 4, 3, 4, 4, 5,                                                                                                                 3, 5, 3, 5, 5, 5, 3, 5, 5, 5, 5, 4, 4, 5, 4, 5, 4, 4, 5, 5, 5, 3, 4, 4, 5, 5, 5,                                                                                                                 4, 4, 4, 4, 4, 6, 4, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 4, 4, 5, 6, 5, 5, 4, 3, 5, 4                                                                                                                , 3, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 5, 5, 4, 4, 6, 5, 5, 4, 5, 4, 5, 5, 4, 4, 4,                                                                                                                 3, 4, 4, 5, 4, 5, 4, 5, 4, 4, 4, 5, 4, 5, 5, 4, 5, 5, 6, 5, 4, 3, 5, 5, 4, 4, 4,                                                                                                                 4, 5, 6, 3, 5, 5, 4, 6, 5, 4, 4, 4, 4, 4, 1, 3, 3, 5, 4, 5, 5, 4, 4, 5, 3, 4, 4                                                                                                                , 2, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 4, 5]


import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from datastructuur import data, node, linkedList
from helper import helper


def makeSequence(mel):
	newMel = []
	j = 0
	for i in range(1,len(mel)):
		if (abs(mel[i] - mel[i - 1]) is not 1):
			newMel.append(mel[j:i])
			j = i
	newMel.append(mel[j:])
	return newMel

def sequenceSwap(start,end,melSequence):
	if start > end:
		start, end = end, start

	melSequence = copy.copy(melSequence)
	newMelSequence = melSequence[:start]
	check = 0
	if end is len(melSequence) - 1:
		newMelSequence.extend([melSequence[end][::-1]])
		end -= 1
		check +=1
	for i in range(end - start + 1):
		newMelSequence.append(melSequence[end - i][::-1])
	if not check:
		newMelSequence.extend(melSequence[end + 1:])

	return newMelSequence

def swapAllSequence(melSequence):
	melSequence = copy.copy(melSequence)
	newMelList = []
	for i in range(len(melSequence)):
		selfSwap = melSequence[:i] + [melSequence[i][::-1]] + melSequence[i+1:]

		newMelList.append(selfSwap)
		for j in range(i):
			newMelList.append(sequenceSwap(j,i,melSequence))
	return newMelList

def makeList(seq):
	List = []
	for i in seq:
		for j in range(len(i)):
			List.append(i[j])
	if type(List[0]) is list:
		makeList(List)
	return tuple(List)

def breadthFirstWithSequences(mel,mir):
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
        		seq = makeSequence(gen)
        		allSwaps = swapAllSequence(seq)

        		for swap in allSwaps:
        			swap = makeList(swap)
        			if swap not in melSet:
        				melSet.add(swap)
        				melList.append(swap)

		

    return melListHistory, swaps




length = 9
gen1 = [*range(1,length + 1)]
gen2 = [*range(1, length + 1)]
rm.shuffle(gen2)

print(breadthFirstWithSequences([9,8,7,6,5,4,3,2,1],gen1))