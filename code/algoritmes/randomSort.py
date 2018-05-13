import random as rm

# from datastructuur import data, node, linkedList
from helper import helper

def randomSort(mel, mir):

	# run until mel and mir are the same
	#while mel != mir:

	# generate random numbers
	i = 0

	while mel != mir:

		a = rm.randint(0,24)
		b = rm.randint(0,24)

		if a > b:
			b, a = a, b

		helper.swapMel(a, b, mel)
		i += 1

		print(i)
		
	print(mel)
