from helper import helper
import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

def mutateGood(mel, int, swapList):
	mel_len = len(mel)
	for i in range(int):
		a = rm.randint(0, mel_len - 1)
		b = rm.randint(0, mel_len - 1)

		swappedMel = helper.swapped(a, b, mel)

		swapList.append(swappedMel)

	return swapList

def scoreNeighbours(swapList, scoreList):

	length = len(swapList)
	for i in range(length):

		score = 0

		for j in range(24):

			checkLeft = swapList[i][j] - swapList[i][j - 1]
			checkRight = swapList[i][j] - swapList[i][j + 1]

			if abs(checkLeft) == 1:
				score += 1
			if abs(checkRight) == 1:
				score += 1

		scoreList.append(score)

	return scoreList

# make an ordered tuple combining scoreList with swapList
def makeTuple(tupleSwap, scoreList, swapList):
	for i in range(len(swapList)):
		tupleSwap.append((scoreList[i], swapList[i]))

	return tupleSwap

# genetic algorithm
def geneticAlgorithm(sampleSize, mel, mir):

	# define databases
	generation = [(0,[])]
	orderedTuple = [(0,[])]

	count = 0
	bestMel = mel

	while orderedTuple[-1][1] is not mir:

		# mutate from best mel X amount of new children
		swapList = mutateGood(bestMel, sampleSize, [])

		# calculate and append score to new children
		scoreList = scoreNeighbours(swapList, [])

		# manipulate data so that score and children are connected in a tuple
		tupleSwap = makeTuple([], scoreList, swapList)

		# order tuple from low score to high score
		orderedTuple = sorted(tupleSwap)

		# define new and previous best score
		newBestScore = orderedTuple[-1][0]

		prevBestScore = generation[-1][0]

		# take the last item in ordered list tuple to get te best score and it's gene row
		best = (orderedTuple[-1][0], orderedTuple[-1][1])

		# if new generated gene row is better then previous append new as new best
		if prevBestScore < newBestScore:

			generation.append(best)

			# continue with new gene row to mutate
			bestMel = orderedTuple[-1][1]

		count += 1
		print(count)
		print(generation)

	return generation
