import random as rm
import math as m
import copy

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from helper import helper
from datastructuur import data, node, linkedList
from helper import helper
# from pancakeSort import pancakeSort
from randomSort import randomSort
from genetic import geneticAlgorithm

import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

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

def scoreNeighbours(swapList, scoreList, mir):

	length = len(swapList)
	for i in range(length):

		score = 0

		for j in range(24):

			checkLeft = swapList[i][j] - swapList[i][j - 1]
			checkRight = swapList[i][j] - swapList[i][j + 1]

			placeMel = swapList[i][j]
			placeMir = mir[j]

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

#_______________________________________________________________________________#

def scoreTest(swapList, scoreList, mir):

	length = len(swapList)

	# iterate over array
	for i in range(length):
		score = 0
		correctessCounter = 1

		for j in range(24):
			checkLeft = swapList[i][j - 1]
			checkRight = swapList[i][j + 1]
			#
			# checkLeft = mel[i-1]
			# checkRight = mel[i+1]

			upperValue = swapList[i][j] + 1

			if upperValue == 26:
				upperValue = 25

			lowerValue = swapList[i][j] - 1

			# check values of right and left
			tempScore = 0

			if lowerValue > 0:
				if swapList[i][j] == j:
					correctessCounter += 1

				if checkLeft == lowerValue or checkLeft == upperValue:
					correctessCounter += 1

				elif checkRight == upperValue:
					# look for location of expected value in array & determine distance between expected location and where value is found
					location = swapList[i].index(lowerValue)
					distance = i - location
					if distance < 0:
						distance *= -1
					tempScore += (distance*distance)

				else:
					# look for location of expected value in array & determine distance between expected location and where value is found
					location = swapList[i].index(upperValue)
					distance = i - location
					if distance < 0:
						distance *= -1
					tempScore += (distance*distance)

			if checkRight == upperValue or checkRight == lowerValue:
				correctessCounter += 1

			elif checkLeft == lowerValue:
				# look for location of expected value in array & determine distance between expected location and where value is found
				location = swapList[i].index(upperValue)
				distance = i - location
				if distance < 0:
					distance *= -1
				tempScore += (distance*distance)

			else:
				# look for location of expected value in array & determine distance between expected location and where value is found
				if lowerValue > 0:
					location = swapList[i].index(lowerValue)
					distance = i - location
				else:
					distance = 0

				if distance < 0:
					distance *= -1
				tempScore += (distance*distance)

				tempScore /= correctessCounter
				score += tempScore

			#
			# score *= -1

			scoreList.append(score)
	return scoreList

#_______________________________________________________________________________#


# genetic algorithm
def geneticAlgorithm(sampleSize, mel, mir):

	# define databases
	generation = [(0,[])]
	orderedTuple = [(0,[])]

	count = 0
	bestMel = mel

	lastGen = mel

	# visualization prints
	# print("Start of with Mel:", mel)
	# print("Run algorithm so that Mel turns in to Mir:", mir)
	# time.sleep(0.5)
	#
	# print("Finding best mutated Mel per iteration out of the population size:", sampleSize)
	# time.sleep(0.5)

	while lastGen != mir:

		# mutate from best mel X amount of new children
		swapList = mutateGood(bestMel, sampleSize, [])

		# calculate and append score to new children
		# scoreList = scoreNeighbours(swapList, [], mir)
		scoreList = scoreTest(swapList, [], mir)

		# manipulate data so that score and children are connected in a tuple
		tupleSwap = makeTuple([], scoreList, swapList)

		# order tuple from low score to high score
		orderedTuple = sorted(tupleSwap)
		# orderedTuple = tupleSwap.sort(reverse=True)
		# print(orderedTuple)

		# define new and previous best score
		newBestScore = orderedTuple[-1][0]

		prevBestScore = generation[-1][0]

		# take the last item in ordered list tuple to get te best score and it's gene row
		best = (orderedTuple[-1][0], orderedTuple[-1][1])

		# if new generated gene row is better then previous append new as new best
		if prevBestScore < newBestScore:

			generation.append(best)

			# visualization
			print("Best Found [(score, genrow)]:", best, ", Mutation number:", count+1)
			time.sleep(0.5)

			# continue with new gene row to mutate
			bestMel = orderedTuple[-1][1]

			lastGen = generation[-1][1]

		count += 1

	return ("Winning Generation[(score, genrow), (nextBestScore, nextBestGenRow), ...]:"), generation, ("Amount of mutations needed:"), count


# print(mutateGood(data.mel, 2, []))
print(geneticAlgorithm(1000, data.mel, data.mir))

# testArray1 = [2,3,1,4,5]
# testArray2 = [3,2,1,5,4]
# testArray3 = [1,2,3,4,5]
# print(scoreTest2(testArray1))
# print(scoreTest2(testArray2))
# print(scoreTest2(testArray3))
