from helper import helper
import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np


def swapped(i,j,mel):
	if j > i:
		i,j = j,i
	return mel[:j] + mel[j:len(mel) - i + j + 1][::-1] + mel[len(mel)+ j - i + 1:]

def swappedTest(i,j,mel):
	if j > i:
		i,j = j,i
	return mel[:j] + mel[j:i + 1][::-1] + mel[1 + i:]

def mutate(mel, int, swapList, mutationPoints):

	mel_len = len(mel)

	for i in range(int):

		a = rm.randint(0, mel_len - 1)
		b = rm.randint(0, mel_len - 1)

		swapMagnitude = abs(a - b) + 1

		swappedMel = swapped(a, b, mel)

		swapList.append(tuple(swappedMel))
		mutationPoints.append(swapMagnitude)

	return swapList, mutationPoints

def scoreNeighbours(swapList, scoreList, mir):

	length = len(swapList)
	for swap in swapList:

		score = 0

		for j in range(24):

			checkLeft = swap[j] - swap[j - 1]
			checkRight = swap[j] - swap[j + 1]

			# does position to check has the right neighbours? if yes add score
			if abs(checkLeft) == 1:
				score += 1
			if abs(checkRight) == 1:
				score += 1

		scoreList.append(score)

	return scoreList

# make an ordered tuple combining scoreList with swapList
def makeTuple(tupleSwap, scoreList, swapList, pointsList):
	i = 0
	for swap in swapList:
		tupleSwap.append((scoreList[i], swap, pointsList[i]))
		i+=1

	return tupleSwap


def swapMel(a, b, mel):

	mel[a:b + 1] = mel[a:b + 1][::-1]

	return mel

# function to check is list is reversed
def isReversed(mel):
	for i in range( len(mel) - 1 ):
		if mel[i] < mel[i+1]:
			return False
		return True

def populationBased(populationSize, mel, mir):
	'''
	Mutates N(populationSize) random gene rows from the mel, calculate the
	score per gene row, choose best gene row, mutate from that best gene row N
	(populationSize). This continues until the best gene found is the solution
	(mir).
					Arguments:
					------------------------------------------------------------
	populationSize: Integer value that signifies the magnitude of the population
	 				size.
					------------------------------------------------------------
	mel: 			The gene row list where to start from.
					------------------------------------------------------------
	mir: 			The gene row list where to finish.
					------------------------------------------------------------

					Returns:
					------------------------------------------------------------
	Generation: 	List containing all best found generows and their scores
					that brought to the solution.
					------------------------------------------------------------
	Count: 			Integer value that signifies the amount of mutations needed.
					------------------------------------------------------------
	'''

	with open('resultaten/population.txt', 'w') as f:

		print('POPULATION BASED ALGORITHM', file=f)
		print('-----------------------------', file=f)
		print('-----------------------------')
		print('POPULATION BASED ALGORITHM')
		print('-----------------------------')

		print("Start of with Mel:", mel)
		print(' '.join(('Start off with Mel:', str(mel))), file=f)
		print("Run algorithm so that Mel turns in to Mir:", mir)
		print(' '.join(('Run algorithm so that Mel turns in to Mir:', str(mir)))
				, file=f)

		print("Finding best mutated Mel per iteration out of the population"
			+ "size:", populationSize)
		print(' '.join(('Finding best mutated Mel per iteration out of the"
			+ " population size:', str(populationSize))), file=f)

		generation = [(0,())]

		count = 0

		bestMel = mel

		lastGen = mel

		points = 0

		while lastGen != mir:

			# mutate from best mel X amount of new children
			swapsAndPoints = mutate(bestMel, populationSize, [], [])

			swapList = swapsAndPoints[0]

			pointsList = swapsAndPoints[1]

			# make a set of the swapList so it deletes doubles
			swapList = set(swapList)

			# calculate and append score to new children
			scoreList = scoreNeighbours(swapList, [], mir)

			# manipulate data so that score and children are
			# connected in a tuple
			tupleSwap = makeTuple([], scoreList, swapList, pointsList)

			# order tuple from low score to high score
			orderedTuple = sorted(tupleSwap)

			# define new and previous best score
			newBestScore = orderedTuple[-1][0]

			prevBestScore = generation[-1][0]

			# take the last item in ordered list tuple to get te best
			# score and it's gene row
			best = (orderedTuple[-1][0], orderedTuple[-1][1],
			 		orderedTuple[-1][2])

			# if new generated gene row is better then previous append
			# new as new best
			if prevBestScore <= newBestScore:
				generation.append(best)

				# continue with new gene row to mutate
				bestMel = list(orderedTuple[-1][1])
				lastGen = list(generation[-1][1])
				points += orderedTuple[-1][2]

				print("Best Found (score, [genrow], mutationPoints):", best,
					  ", Mutation number:", count+1)
				print(' '.join(('Best Found (score, [genrow], mutationPoints):'
					  , str(best), ", Mutation number:", str(count+1))), file=f)

			count += 1

		# check if reversed is true, if yes swap to ascending order
		reversed = isReversed(lastGen)
		if reversed == True:
			swapMel(24,0,lastGen)

		print(' '.join(('Winning Generation[(score, genrow), (nextBestScore,'
			+ 'nextBestGenRow), ...]:', str(generation))), file=f)
		print(' '.join(('Amount of mutations needed:', str(count))), file=f)
		print(' '.join(('Mutation points:', str(points))), file=f)

		print('-----------------------------')
		print('-----------------------------', file=f)
		print('RESULT')
		print('RESULT', file=f)
		print('-----------------------------')
		print('-----------------------------', file=f)

	return ("Winning Generation[(score, genrow),"
	      + " (nextBestScore,' nextBestGenRow), ...]:"),
		   generation, ("Amount of mutations needed:"), count
