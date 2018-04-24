import random as rm
import math as m
import sys
import copy

mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


# define swap function
def swapMel(a, b, mel):
	mel[a:b + 1] = mel[a:b + 1][::-1]

# random generator
def randomGen(mel, mir):

	# run until mel and mir are the same
	#while mel != mir:

	# generate random numbers
	a = rm.randint(0,24)
	b = rm.randint(0,24)


	if a > b:
		b, a = a, b

	print(mel[a])
	print(mel[b])
	print(mel)

	# call swap function
	swapMel(a, b, mel)

	print(mel)


def pancakeSort(mel, mir):
	swapCount = 0
	mel_len = len(mel)
	mir_len = len(mir)
	if mel_len is not mir_len:
		message = "error, lists are not the same length"
		return message
	else:
		for i in range(mel_len):
			if mir[i] is not mel[i]:
				for j in range(i,mel_len):
					if mir[i] is mel[j]:
						mel = swapMel(i,j,mel)
						swapcount += 1
	print(mel)
	print(swapCount)

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

		print(mel[a:b])
		
		swapMel(a,b,melTemp)
		
		swapList.append(melTemp)



	print(swapList)
	return swapList

beamSearch(mel,mir)


class data:
	def __init__(self):
		self.swaplist = []
		self.correctness = 0

	def addCorr(self, corr):
		self.correctness += corr

	def minCorr():
		self.correctness -= 1


def gen(mel, int):

	# 10 random swaps genereren -> array vullen met random swapped
	array = []

	for i in range(int):

		a = rm.randint(0,len(mel)-1)
		b = rm.randint(0,len(mel)-1)


		temp = swapMel(a, b, mel)
		print("temp: ",temp)
		array.append(temp)


	return array
