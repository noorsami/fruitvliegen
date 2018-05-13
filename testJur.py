import random as rm
import math as m
import copy

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


from datastructuur import data, node, linkedList
from helper import helper
from mutate import *
from listGen import *
from pancakeSort import pancakeSort
from beamSearch import beamSearch
from listGen import *
from mutate import *
from randomSort import randomSort

def genTable(mel, int, listGen):
	array = []
	for mel in listGen(mel, int):
		ll = linkedList()
		ll.addNode(mel, 0, 0)
		array.append(ll)
	return array

def muTable(table, rate, mutation):
	for i in range(rate):
		for ll in table:
			node = ll.currNode
			swapMel = mutation(node.swapMel)
			scoreX = score(swapMel)
			swaps = node.swaps
			swaps += 1
			ll.addNode(swapMel, scoreX, swaps)

def checkTable(table):
	for i in range(rate):
		for ll in table:
			if ll.next is None:
				return ll.score
			else:
				return min(ll.score, get_min(ll.score))

def get_min(ll):
    if ll.next is None:
        return ll.score
    else:
        return min(ll.score, get_min(ll.score))






def printTable(table):
	for i in range(len(table)):
		print("Bucket nr: ", + (i+1))
		table[i].listPrint()
		print(" ")

def score(mel):
	score = 0
	for i in range(24):
		# staat genoom op goede plek?
		if mel[i] is i+1:
			score += 1
		# is het rechtergenoom naast mel (mel +1)?
		if mel[i+1] is mel[i] + 1:
			score += 1
		# is het linkergenoom naast mel (mel-1)?
		if mel[i-1] is mel[i] - 1:
			score += 1
	return score

def score2(mel):
	score = 0
	for i in range(24):
		# staat genoom op goede plek?
		if mel[i] is i+1:
			score += 1

		if mel[i+1] is mel[i] + 1 and mel[i-1] is mel[i] - 1:
			score += 1

	return score


# def checkTable(table):
# 	for ll in table:
# 		max, node = ll.Max()
# 		node.next = None
# 		print(node.swapMel, + node.score)
# 	return table

































table = genTable(data.mel, 10, listGen.genX)
muTable(table, 10, mutate.random)
# checkTable(table)
printTable(table)
