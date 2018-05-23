

import random as rm
import math as m
import copy

from datastructuur import data
from helper import helper
from score import score
from pancakeSort import pancakeSort
from randomSort import randomSort
from population import populationBased
from simulatedAnnealing import simulatedAnnealing


class tester:

    def pancakeSort():
        for i in range(100):
            print("\n--------------------------------------")
            print("              Set nr:" + str(i+1))
            print("--------------------------------------\n")
            randomSeq = [*range(1,26)]
            rm.shuffle(randomSeq)
            pancakeSort(randomSeq, data.mir)

    def populationBased():
        for i in range(100):
            print("\n--------------------------------------")
            print("              Set nr:" + str(i+1))
            print("--------------------------------------\n")
            randomSeq = [*range(1,26)]
            rm.shuffle(randomSeq)
            print(populationBased(300, randomSeq, data.mir))

    def simulatedAnnealing():
        for i in range(100):
            print("\n--------------------------------------")
            print("              Set nr:" + str(i+1))
            print("--------------------------------------\n")
            randomSeq = [*range(1,26)]
            rm.shuffle(randomSeq)
            print("Starting with: \n", randomSeq)
            simulatedAnnealing(randomSeq, data.mir, 1000, score.scoreNeighbours)
