import random as rm
import math as m
import copy
import matplotlib.pyplot as plt
import numpy as np

from helper import helper
from tester import tester
from score import score
from pancakeSort import pancakeSort
from randomSort import randomSort
from population import populationBased
from simulatedAnnealing import simulatedAnnealing
from steepestDescendValleyAbseiler import steepestDescendValleyAbseiler

class visualize:

    def populationVisualizer(startingPoint):
        '''
            Function for the visualization of the mean amount of mutations
            needed when running the population based algorithm.

        	                Arguments:
            	            ----------------------------------------------------
            startingPoint:  The genome sequence where to start from, can be
                            either the melanogaster in the default case or the
                            random set in the tester case

                            Returns:
                            ----------------------------------------------------
            Barchart:       Barchart with on the X axis the different parameters
                            and on the Y axis the mean amount of mutations
                            needed.
        '''
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

        plt.bar(sampleSizes, populationMean, align = 'center')
        plt.title("100 times from random sequence to Miranda")
        plt.ylabel("average amount of mutations needed")
        plt.xlabel("sample size")
        plt.show()

        return sampleSizes, populationMean


    def simulatedVisualizer(startingPoint):
        '''
            Function for the visualization of the mean amount of mutations
            needed when running the simulated algorithm.

        	                Arguments:
            	            ----------------------------------------------------
            startingPoint:  The genome sequence where to start from, can be
                            either the melanogaster in the default case or the
                            random set in the tester case

                            Returns:
                            ----------------------------------------------------
            Barchart:       Barchart with on the X axis the different parameters
                            and on the Y axis the mean amount of mutations
                            needed.

        '''

        failValues = [1000, 10000, 100000]

        test = tester.simulatedTester

        simulatedMean = [test(failValues[0], startingPoint),
                         test(failValues[1], startingPoint),
                         test(failValues[2], startingPoint)]

        print(failValues)

        plt.bar(failValues, simulatedMean, align = 'center')
        plt.title("100 times from random sequence to Miranda")
        plt.ylabel("average amount of mutations needed")
        plt.xlabel("fail value")
        plt.show()

    def combinedVisualizer(mel, mir):
        '''
            Function for the visualization of the mean amount of mutations
            needed when running the algorithm in default.
            It takes the melanogaster and the miranda as arguments and runs
            them through the different algorithm testers.
            Takes the output for the execution of the visualization.

        	              Arguments:
            	          ------------------------------------------------------
            mel:          The genome sequence of the Drosophila Melanogaster,
                          with which the algorithm starts it's mutation sequence.
            	          ------------------------------------------------------
            mir:          The genome sequence of the Drosophila Miranda, which
                          is theintended target of the sorts on the Melanogaster.
            			  The algorithm stops once it has sorted the
                          Melanogaster-sequence into the genome sequence
                          of the Miranda.

                          Returns:
                          ------------------------------------------------------
            Barchart:     Barchart with on the X axis the different algorithms
                          and on the Y axis the amount of mutations needed.

        '''

        population = tester.populationTester(300, mel)
        simulated = tester.simulatedTester(1000, mel)
        steepest = steepestDescendValleyAbseiler(mir, mel)
        pancake = pancakeSort(mel, mir)


        names = ['pancakeSort', 'populationBased', 'simulatedAnnealing', 'SDVA']
        output = [pancake[1], population, simulated, steepest[1]]

        plt.bar(names, output, align = 'center')
        plt.title("Algorithm vs. Algorithm")
        plt.ylabel("Amount of mutations needed")
        plt.show()


    def SDVAVisualizer(mir,mel):
        data = steepestDescendValleyAbseiler(mir,mel)
        history = data[0]
        swaps = data[1]
        swapLen = data[2]

        fig = plt.figure()
        title = "steepestDescend; N = " + str(len(mir))
        plt.subplot(211)
        plt.plot(range(len(history)),history, label = "Sequences")
        plt.xticks(np.arange(0, len(history), 1))
        plt.xlabel("Number of swaps")
        plt.ylabel("Number of sequences in generation")
        plt.title(title)
        plt.subplot(212)
        plt.plot(range(len(swapLen)),swapLen, label = "Sequences")
        plt.xticks(np.arange(0, len(swapLen), 1))
        plt.xlabel("Number of swaps")
        plt.ylabel("Length of smallest sequence")
        plt.show()
        
