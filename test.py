import matplotlib.pyplot as plt
import random as rm
import math as m
import sys

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
		
	print mel[a] 
	print mel[b]
	print mel
		
	# call swap function
	swapMel(a, b, mel)
		
	print mel


def hasjSort(mel, mir):
	swapcount = 0
	for i in range(len(mel)): 
		for j in range(i, len(mel)):
			if mel[i] > mel[j]:	
				swapMel(i, j, mel)
				print mel
		swapcount += 1
	print swapcount

hasjSort(mel, mir)





