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
from pancakeSort import pancakeSort
from beamSearch import beamSearch
from randomSort import randomSort

def beamSearch(mel, mir):

	swaps = helper.gen(mel, 10)
	array = []


onzin = ["bla"]
	
def genTable(mel, int):

	array = []
	for mel in helper.gen(mel, int):

		ll = linkedList()
		ll.addNode(mel)

		array.append(ll)
	return array

def printTable(table):
	for i in range(len(table)):
		table[i].listPrint()
		print(" ")

def mutate(mel):
	melTemp = copy.copy(mel)
	a, b = helper.randomGen()

	if a > b:
		b, a = a, b

	melTemp = helper.swapMel(a,b, melTemp)
	return melTemp

def muTable(table, rate):
	for i in range(rate):
		for ll in table:
			node = ll.currNode
			swapMel = node.swapMel
			swapMel = mutate(node.swapMel)
			ll.addNode(swapMel)

table = genTable(data.mel, 10)
muTable(table, 10)
printTable(table)

# print(data.mel)
# print(mutate(data.mel))


