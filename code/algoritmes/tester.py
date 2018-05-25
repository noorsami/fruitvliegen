

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

    def pancakeTester(startingPoint):
        count = 0
        for i in range(100):
            print("\n-------------------------------------")
            print("             Set nr:" + str(i+1))
            print("-------------------------------------\n")
            if startingPoint != data.mel:
                rm.shuffle(startingPoint)

            pancake = pancakeSort(startingPoint, data.mir)
            print(pancake[0])
            print(pancake[1])
            count += pancake[1]
        print("Average amount of mutations needed for this test:", count/100)
        return count/100

    def populationTester(sampleSize, startingPoint):
        count = 0
        for i in range(100):
            print("\n-------------------------------------")
            print("             Set nr:" + str(i+1))
            print("-------------------------------------\n")
            #randomSeq = [*range(1,26)]
            if startingPoint != data.mel:
                rm.shuffle(startingPoint)
            population = populationBased(sampleSize, startingPoint, data.mir)
            print(population[0])
            print(population[1])
            count += population[1]
        print("Average amount of mutations needed for this test:", count/100)
        return count/100

    def simulatedTester(failValue, startingPoint):
        count = 0
        for i in range(100):
            print("\n-------------------------------------")
            print("             Set nr:" + str(i+1))
            print("-------------------------------------\n")
            if startingPoint != data.mel:
                rm.shuffle(startingPoint)
            print("Starting with: \n", startingPoint)
            sim = simulatedAnnealing(startingPoint, data.mir, failValue,
                                     score.scoreNeighbours)
            print(sim[0])
            print(sim[1])
            count += sim[1]
        print("Average amount of mutations needed for this test:", count/100)
        return count/100
