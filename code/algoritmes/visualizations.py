import random as rm
import math as m
import copy
import matplotlib.pyplot as plt

from helper import helper
from tester import tester
from score import score
from pancakeSort import pancakeSort
from randomSort import randomSort
from population import populationBased
from simulatedAnnealing import simulatedAnnealing

class visualize:

    def populationVisualizer(startingPoint):

        sampleSizes = [50, 100, 150, 300, 500, 750, 1000]

        test = tester.populationTester

        populationMean = [test(sampleSizes[0], startingPoint),
                          test(sampleSizes[1], startingPoint),
                          test(sampleSizes[2], startingPoint),
                          test(sampleSizes[3], startingPoint),
                          test(sampleSizes[4], startingPoint),
                          test(sampleSizes[5], startingPoint),
                          test(sampleSizes[6], startingPoint)]

        print(sampleSizes)
        print(populationMean)

        plt.plot(sampleSizes, populationMean)
        plt.ylabel("average amount of mutations needed")
        plt.xlabel("sample size")
        plt.title("100 times from random sequence to Miranda")
        plt.show()

        return sampleSizes, populationMean


    def simulatedVisualizer():

        failValues = [1000, 10000, 100000]

        test = tester.simulatedTester

        simulatedMean = [test(failValues[0]),
                         test(failValues[1]),
                         test(failValues[2])]

        print(failValues)

        plt.plot(failValues, simulatedMean)
        plt.ylabel("average amount of mutations needed")
        plt.xlabel("fail value")
        plt.title("100 times from random sequence to Miranda")
        plt.show()
