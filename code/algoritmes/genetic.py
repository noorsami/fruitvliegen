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

			# does position to check has the right neighbours? if yes add score
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

# function to check is list is reversed
def isReversed(mel):
	for i in range( len(mel) - 1 ):
		if mel[i] < mel[i+1]:
			return False
		return True

# function for swap if reversed is true
def swapMel(a, b, mel):
	mel[a:b + 1] = mel[a:b + 1][::-1]
	return mel

# genetic algorithm
def geneticAlgorithm(populationSize, mel, mir):

	# open results textfile
	#with open('resultaten/genetic.txt', 'w') as f:

	#print('GENETIC ALGORITHM', file=f)

	# define databases
	generation = [(0,[])]
	orderedTuple = [(0,[])]

	count = 0
	bestMel = mel

	lastGen = mel

		# visualization
		#print("Start of with Mel:", mel)
		#print(' '.join(('Start off with Mel:', str(mel))), file=f)
		#print("Run algorithm so that Mel turns in to Mir:", mir)
		#print(' '.join(('Run algorithm so that Mel turns in to Mir:', str(mir))), file=f)
		#time.sleep(0.5)

		#print("Finding best mutated Mel per iteration out of the population size:", populationSize)
		#print(' '.join(('Finding best mutated Mel per iteration out of the population size:', str(populationSize))), file=f)

	while lastGen != mir:

			# mutate from best mel X amount of new children
		swapList = mutateGood(bestMel, populationSize, [])

			# calculate and append score to new children
		scoreList = scoreNeighbours(swapList, [], mir)

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

				# visualization
				#print("Best Found (score, [genrow]):", best, ", Mutation number:", count+1)
				#print(' '.join(('Best Found (score, [genrow]):', str(best), ", Mutation number:", str(count+1))), file=f)
				#time.sleep(0.5)

				# continue with new gene row to mutate
			bestMel = orderedTuple[-1][1]

			lastGen = generation[-1][1]

		count += 1

		# check if reversed is true, if yes swap to ascending order
		reversed = isReversed(lastGen)
		if reversed == True:
			swapMel(0,24,lastGen)

		print(generation)
		print(count)
		# visualization
		#print(' '.join(('Winning Generation[(score, genrow), (nextBestScore, nextBestGenRow), ...]:', str(generation))), file=f)
		#print(' '.join(('Amount of mutations needed:', str(count))), file=f)


	return ("Winning Generation[(score, genrow), (nextBestScore, nextBestGenRow), ...]:"), generation, ("Amount of mutations needed:"), count
