import random as rm
import math as m
import copy

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from datastructuur import data, node, linkedList
from helper import helper
from pancakeSort import pancakeSort
from beamSearch import beamSearch
from randomSort import randomSort

# def gen(mel, int):

# 	mel_len = len(mel)
# 	swapList = []

# 	for i in range(int):
# 		melTemp = copy.copy(mel)
# 		a = rm.randint(0, mel_len - 1)
# 		b = rm.randint(0, mel_len - 1)

# 		if a > b:
# 			b, a = a, b

# 		melTemp = helper.swapMel(a,b,melTemp)
		
# 		swapList.append(melTemp)

# 	return swapList

# print(gen(data.mel, 10))

beamSearch(data.mel, data.mir)