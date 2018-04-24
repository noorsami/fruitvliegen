import random as rm
import copy

from datastructuur import data, node, linkedList
from helper import helper

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