#  nordin

import random as rm
import math as m
import sys
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


# define swap function
def swapMel(a, b, mel):
	mel[a:b + 1] = mel[a:b + 1][::-1]
	return mel

# random generator
def randomGen(mel, mir):
	# run until mel and mir are the same
	i = 0
	while mel != mir:

		# generate random numbers
		a = rm.randint(0,24)
		b = rm.randint(0,24)


		if a > b:
			b, a = a, b

		# call swap function
		swapMel(a, b, mel)
		i += 1
		print(i)

	print(mel)

def pancakeSort(mel, mir):

	print("Start off with Mel:", mel)
	print("Run algorithm so that Mel turns in to Mir:", mir)

	swapCount = 0
	mel_len = len(mel)
	mir_len = len(mir)
	if mel_len is not mir_len:
		message = "error, lists are not the same length"
		return message
	else:
		for i in range(mel_len):

			#plt.plot(mir, mel, mir, mir)
			#plt.axis([1,25, 1, 25])
			#plt.show()

			if mir[i] is not mel[i]:
				for j in range(i,mel_len):
					if mir[i] is mel[j]:
						mel = swapMel(i,j,mel)
						print("Swap", swapCount, ":", mel)

						#plt.show()

						swapCount += 1
						time.sleep(0.5)
	print("Final Swap:", mel)
	print("Number of swaps:", swapCount)

	return mel


def beamSearch(mel, mir):
	mel_len = len(mel)
	mir_len = len(mir)
	swapList = []

	for i in range(10):
		melTemp = copy.copy(mel)
		a = rm.randint(0, mel_len - 1)
		b = rm.randint(0, mir_len - 1)

		if a > b:
			b, a = a, b

		swapMel(a,b,melTemp)

		swapList.append(melTemp)

	print(swapList)
	return swapList



def randomGen():
	a = rm.randint(0,24)
	b = rm.randint(0,24)
	return a, b


### GENETIC ALGORITHM TESTS

swapList = []

# generates x arrays with random mutations from mel
def genRandom(mel, int):

	mel_len = len(mel)

	for i in range(int):
		melTemp = copy.copy(mel)
		a = rm.randint(0, mel_len - 1)
		b = rm.randint(0, mel_len - 1)

		if a > b:
			b, a = a, b

		melTemp = swapMel(a,b,melTemp)

		swapList.append(melTemp)

	return swapList


genRandom(mel,10)

scoreList = []
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

	scoreList.append(score)
	return score


generation = []
def selection(scoreList, swapList):

	for j in range(len(swapList)):
		score(swapList[j])

	print(swapList)
	print(scoreList)

	## get index
	for i in range(len(scoreList)):
		if scoreList[i] == max(scoreList):
			winner = swapList[i]
			generation.append(winner)

	print(len(swapList))
	print(winner)
	print(generation)

	swapList = []
	genRandom(winner, 10)

	print(swapList)
	print(len(swapList))

	#for i in range(len(scoreList) - 1, 0 , -1):

	#	if scoreList[i] >= max(scoreList):
	#		break;

	#	swapList.pop()


	return swapList

mel_len = len(mel)

selection(scoreList, swapList)

#database = []

#lijst = [(1, [1, 2]), (0, [4, 4])]
#ordered = sorted(lijst)
#best = ordered[-1][1]
