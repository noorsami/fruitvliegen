from helper import helper

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
		# is het rechtergenoom naast mel (mel +1)?
		if mel[i+1] is mel[i] + 1:
			score += 1
		# is het linkergenoom naast mel (mel-1)?
		if mel[i-1] is mel[i] - 1:
			score += 1

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
		scoreList.append(score(swapList[i], []))

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
		best = (orderedTuple[-1][0], orderedTuple[-1][1])

		# if new generated gene row is better then previous append new as new best
		if prevBestScore < newBestScore:
			generation.append(best)

			# continue with new gene row to mutate
			bestMel = orderedTuple[-1][1]

		count += 1
		print(count)

	return generation
