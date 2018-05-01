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

def printTable(table):
	for i in range(len(table)):
		table[i].listPrint()
		print(" ")

def genTable(mel, int, listGen):

	array = []
	# for mel in helper.genRandom(mel, int):
	for mel in listGen(mel, int):

		ll = linkedList()
		ll.addNode(mel)

		array.append(ll)
	return array

def muTable(table, rate, mutation):
	for i in range(rate):
		for ll in table:
			node = ll.currNode
			swapMel = node.swapMel
			swapMel = mutation(node.swapMel)
			ll.addNode(swapMel)

table = genTable(data.mel, 10, listGen.genX)
muTable(table, 10, mutate.random)
printTable(table)



# print(data.mel)
# print(mutate(data.mel))


