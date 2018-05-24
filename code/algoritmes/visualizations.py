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

    def populationVisualizer():

        sampleSizes = [50, 100, 150, 300, 500, 750, 1000]

        x = tester.populationTester

        populationMean = [x(sampleSizes[0]),
                          x(sampleSizes[1]),
                          x(sampleSizes[2]),
                          x(sampleSizes[3]),
                          x(sampleSizes[4]),
                          x(sampleSizes[5]),
                          x(sampleSizes[6])]

        print(sampleSizes)
        print(populationMean)

        plt.plot(sampleSizes, populationMean)
        plt.ylabel('average amount of mutations needed')
        plt.xlabel('sample size')
        plt.title('100 times from random gen sequence to the Drosophila Miranda (N=25)')
        plt.show()

        return sampleSizes, populationMean


    def simulatedAnnealing():

        failValues = [1000, 10000, 100000]
