from helper import helper
from score import score
import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

def populationBased(populationSize, mel, mir):
	'''
	A population based optimization algorithm based on genetic algorithms,
	which are metaheuristics inspired by the process of natural selection.
	The optimization consists of mutating the genome sequence of the
	Drosophila Melanogaster into the Drosophila Miranda.

	The algorithm mutates N(populationSize) random gene rows from the mel,
	then calculate the score per gene row and chooses, based on that score,
	the best gene row. This continues witch each new mutation, until the best
	gene found is the solution (mir).

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

	with open("resultaten/population.txt", "w") as f:

		print("POPULATION BASED ALGORITHM", file=f)
		print("-----------------------------", file=f)
		print("-----------------------------")
		print("POPULATION BASED ALGORITHM")
		print("-----------------------------")

		print("Start of with Mel:", mel)
		print(" ".join(("Start off with Mel:", str(mel))), file=f)
		print("Run algorithm so that Mel turns in to Mir:", mir)
		print(" ".join(("Run algorithm so that Mel turns in to Mir:", str(mir)))
				, file=f)

		print("Finding best mutated Mel per iteration out of the population"
		+ "size:", populationSize)
		print(" ".join(("Finding best mutated Mel per iteration out of the"
		+ "population size:", str(populationSize))), file=f)

		generation = [(0,())]
		count = 0
		bestMel = mel
		lastGen = mel

		while lastGen != mir:

			# mutate from best mel X amount of new children
			swapList = helper.mutate(bestMel, populationSize, [])

			# make a set of the swapList so it deletes doubles
			swapList = set(swapList)

			# calculate and append score to new children
			scoreList = score.scoreNeighboursList(swapList, [], mir)

			# manipulate data so that score and children are
			# connected in a tuple
			tupleSwap = helper.makeTuple([], scoreList, swapList)

			# order tuple from low score to high score
			orderedTuple = sorted(tupleSwap)

			# define new and previous best score
			newBestScore = orderedTuple[-1][0]
			prevBestScore = generation[-1][0]

			# take the last item in ordered list tuple to get te best
			# score and it's gene row
			best = (orderedTuple[-1][0], orderedTuple[-1][1])

			# if new generated gene row is better then previous append
			# new as new best
			if prevBestScore <= newBestScore:
				generation.append(best)

				# continue with new gene row to mutate
				bestMel = list(orderedTuple[-1][1])
				lastGen = list(generation[-1][1])

				print("Best Found (score, [genrow], mutationPoints):", best,
					  ", Mutation number:", count+1)
				print(" ".join(("Best Found (score, [genrow], mutationPoints):"
					  , str(best), ", Mutation number:", str(count+1))), file=f)

			count += 1

		# check if reversed is true, if yes swap to ascending order
		reversed = helper.isReversed(lastGen)
		if reversed == True:
			swapMel(24,0,lastGen)

		print(" ".join(("Winning Generation[(score, genrow), (nextBestScore,"
			+ "nextBestGenRow), ...]:", str(generation))), file=f)
		print(" ".join(('Amount of mutations needed:', str(count))), file=f)

		print("-----------------------------")
		print("-----------------------------", file=f)
		print("RESULT")
		print("RESULT", file=f)
		print("-----------------------------")
		print("-----------------------------", file=f)

	return generation, count
