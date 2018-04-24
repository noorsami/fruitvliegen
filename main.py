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

# ll = linkedList()
# ll.addNode(data.mel)
# ll.addNode(data.mir)

# ll.listPrint()

# for i in range(10):
# 	print(data.mel[i])

<<<<<<< HEAD
pancakeSort(data.mel, data.mir)
#beamSearch(data.mel, data.mir)
#randomSort(data.mel, data.mir)
=======
# pancakeSort(data.mel, data.mir)
beamSearch(data.mel, data.mir)
# randomSort(data.mel, data.mir)
>>>>>>> 01fe1f492bc668f22415e485370c78448e75a960

