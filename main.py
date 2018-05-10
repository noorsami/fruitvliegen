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
from genetic import geneticAlgorithm

print("\nWELCOME!\n\n When you want to run the pancake sorting algorithm type in: p \n\n When you want to run the genetic algorithm type in: g\n")

algorithm = input("Type in the algorithm that you want to run: \n\n")

if algorithm == 'p':
    pancake = pancakeSort(data.mel, data.mir)
    print(pancake)

elif algorithm == 'g':
    genetic = geneticAlgorithm(10, data.mel, data.mir)
    print(genetic)

else:
    print("Error, unknown input")
