import random as rm
import math as m
import sys

mel = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# define swap function
def swapMel(a, b, mel):
	mel[a:b + 1] = mel[a:b + 1][::-1]
	return mel

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


def hasjSort(mel, mir):
	swapcount = 0
	mel_len = len(mel)
	mir_len = len(mir)
	if mel_len is not mir_len:
<<<<<<< HEAD
		message = "error, lists are not the same length"
=======
		message = "error lists not same length"
>>>>>>> 0d5c3de14f9ca785bd1ec8a991ee29441f3e90c9
		return message
	else:
		for i in range(mel_len):
			if mir[i] is not mel[i]:
				for j in range(i,mel_len):
					if mir[i] is mel[j]:
						mel = swapMel(i,j,mel)
<<<<<<< HEAD
						swapcount += 1
	print(mel)
	print(swapcount)

	return mel

hasjSort(mel, mir)


=======
	print(mel)
	return mel


hasjSort(mel, mir)
>>>>>>> 0d5c3de14f9ca785bd1ec8a991ee29441f3e90c9