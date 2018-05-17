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
from pancakeSort import pancakeSort
from beamSearch import beamSearch
from randomSort import randomSort
from genetic import geneticAlgorithm

import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np


# generates x arrays with random mutations from mel
def mutate(mel, int, swapList):

	mel_len = len(mel)

	for i in range(int):
		melTemp = copy.copy(mel)
		a = rm.randint(0, mel_len - 1)
		b = rm.randint(0, mel_len - 1)

		if a > b:
			b, a = a, b

		melTemp = helper.swapMel(a,b,melTemp)

		swapList.append(melTemp)

	return swapList

# calculates score per children
def score(mel, scoreList):
	score = 0
	for i in range(24):

		# staat genoom op goede plek?
		if mel[i] is i+1:
			score += 1
		# # is het rechtergenoom naast mel (mel +1)?
		# if mel[i+1] is mel[i] + 1:
		# 	score += 1
		# # is het linkergenoom naast mel (mel-1)?
		# if mel[i-1] is mel[i] - 1:
		# 	score += 1

	scoreList.append(score)

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

# appends score to scorelist
def appendScore(swapList, scoreList):
	for i in range(len(swapList)):
		scoreList.append(scoreTest(swapList[i]))

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
		swapList = mutate(bestMel, sampleSize, [])

		# calculate and append score to new children
		scoreList = appendScore(swapList, [])

		# manipulate data so that score and children are connected in a tuple
		tupleSwap = makeTuple([], scoreList, swapList)

		# order tuple from low score to high score
		orderedTuple = sorted(tupleSwap)

		# define new and previous best score
		newBestScore = orderedTuple[-1][0]

		prevBestScore = generation[-1][0]

		# take the last item in ordered list tuple to get te best score and it's gene row
		best = (orderedTuple[1][0], orderedTuple[1][1])

		# if new generated gene row is better then previous append new as new best
		if prevBestScore < newBestScore:
			generation.append(best)

			# continue with new gene row to mutate
			bestMel = orderedTuple[1][1]

		count += 1
		print(count)

	return generation

# genetic = geneticAlgorithm(10, data.mel, data.mir)
# print(genetic)
#
#




# scorefunctie:

# kijk ipv naar of de neighbours van een waarde correct zijn,
# naar de afstand van de locatie van de getallen die neighbours moeten zijn tov de plek naast de waarde.

def scoreNeighbours(mel):
    score = 0
    length = len(mel)
    for i in range(1, length - 1):
        checkLeft = mel[i] - mel[i - 1]
        checkRight = mel[i] - mel[i + 1]
        if abs(checkLeft) == 1:
            score += 1
        if abs(checkRight) == 1:
            score += 1
    return score


#_______________________________________________________________________________#

def scoreTest(mel):
	score = 0
	length = len(mel)

	correctessCounter = 1
	score = 0

	# iterate over array
	for i in range(1, length - 1):
		checkLeft = mel[i-1]
		checkRight = mel[i+1]

		upperValue = mel[i] + 1
		if upperValue == length +1:
			upperValue = length

		lowerValue = mel[i] - 1

		# determine values that right and left should have
			# both sides can be upper or lower
			# upper = i + 1
			# lower = i - 1

		# check values of right and left
		tempScore = 0

		if lowerValue > 0:
			if mel[i] == i:
				correctessCounter += 1

			if checkLeft == lowerValue or checkLeft == upperValue:
				correctessCounter += 1

			elif checkRight == upperValue:
				# look for location of expected value in array & determine distance between expected location and where value is found
				location = mel.index(lowerValue) + 1
				distance = i - location
				if distance < 0:
					distance *= -1
				tempScore += (distance*distance)

			else:
				# look for location of expected value in array & determine distance between expected location and where value is found
				location = mel.index(upperValue) + 1
				distance = i - location
				if distance < 0:
					distance *= -1
				tempScore += (distance*distance)

		if checkRight == upperValue or checkRight == lowerValue:
			correctessCounter += 1

		elif checkLeft == lowerValue:
			# look for location of expected value in array & determine distance between expected location and where value is found
			location = mel.index(upperValue) + 1
			distance = i - location
			if distance < 0:
				distance *= -1
			tempScore += (distance*distance)

		else:
			# look for location of expected value in array & determine distance between expected location and where value is found
			if lowerValue > 0:
				location = mel.index(lowerValue) + 1
				distance = i - location
			else:
				distance = 0

			if distance < 0:
				distance *= -1
			tempScore += (distance*distance)

		tempScore /= correctessCounter
		score += tempScore

	return score

#_______________________________________________________________________________#


			# look for location of expected value in array & determine distance between expected location and where value is found




	# if value is not correct ( i + 1 or i - 1) --> look for location of expected value in array
	# determine distance between expected location and where value is found

	# --> linear search function which returns the i of the array when the value is found
	# --> location of value - location of expected value = score

	# scoreLeft = distance of left expected values
	# scoreRight = distance of right expected value


	# score per Value = scoreLeft + scoreRight / 2







melTest = [2,1,3]
melTest2 = [9,8,7,6,5,4,3,2,1]
melTarget = [1,2,3]
print(scoreTest(melTest))
print(scoreTest(melTest), melTest)
print(scoreTest(melTest2), melTest2)
print("Target: ", scoreTest(melTarget), melTarget)
#
# geneticAlgorithm(100, melTest, melTarget)
