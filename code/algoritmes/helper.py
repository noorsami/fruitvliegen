
import random as rm
import copy

class helper:

# basic helper functions
	def randomGen():
		a = rm.randint(0,24)
		b = rm.randint(0,24)
		return a, b

	def swapMel(a,b,mel):
		mel[a:b + 1] = mel[a:b + 1][::-1]
		return mel

	def swapped(i,j,mel):
		if j > i:
			i,j = j,i

		return mel[:j] + mel[j:len(mel) - i + j + 1][::-1] + mel[len(mel)+ j - i + 1:]


	# returns all possible swaps
	def swapAll(mel):
	    newMelList = []
	    for i in range(len(mel)):
	        for j in range(i):
	            newMelList.append(tuple(helper.swapped(i,j,mel)))

	    return newMelList

	# checks a list for dublicates and returns a list of lists
	def noDublicates(list):
	    listSet = set(tuple(item) for item in list)
	    noDublicate = []
	    for item in listSet:
	        noDublicate.append(item)
	    return noDublicate
