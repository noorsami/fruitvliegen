import random as rm
import math as m
import copy

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from datastructuur import data
from helper import helper
from pancakeSort import pancakeSort
from randomSort import randomSort
from population import populationBased
from simulatedAnnealing import simulatedAnnealing

print("\nWELCOME!\n\n When you want to run the pancake sorting algorithm type in: 1 \n\n When you want to run the population based algorithm type in: 2 \n\n When you want to run the simulated annealing algorithm type in: 3\n")

algorithm = input("Type in the algorithm that you want to run: \n\n")

if algorithm == '1':
    pancake = pancakeSort(data.mel, data.mir)
    print(pancake)

elif algorithm == '2':
    populationBased = populationBased(300, data.mel, data.mir)
    print(populationBased)

elif algorithm == '3':
    simulated = simulatedAnnealing(data.mel, data.mir, 1000)
    print(simulated)

else:
    print("Error, unknown input")
