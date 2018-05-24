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
from score import score
from pancakeSort import pancakeSort
from randomSort import randomSort
from population import populationBased
from simulatedAnnealing import simulatedAnnealing
from steepestDescendValleyAbseiler import steepestDescendValleyAbseiler
from tester import tester

print("\nWELCOME!\n\n When you want to run the pancake sorting algorithm type in: 1 \
                 \n\n When you want to run the population based algorithm type in: 2 \
                 \n\n When you want to run the simulated annealing algorithm type in: 3 \
                 \n\n When you want to run the Steepest Descend Valley Abseiler algorithm, type in: 4\n")

algorithm = input("Type in the algorithm that you want to run: \n\n")

''' PANCAKESORT '''
if algorithm == '1':
    default = input("\n If you want to run the algorithm with default parameters, type 'd'.\n\n \
                        For running the algorithm on a test-set with 100 random genomes of length 25, type 't' \n\n")

    if default == 'd':
        print(pancakeSort(data.mel, data.mir))
    if default == 't':
        tester.randomTester(pancakeSort)

''' POPULATION BASED '''
if algorithm == '2':
    default = input("\n If you want to run the algorithm once with the default parameters, type 'd'.\n\n \
                        For custom parameters, type 'c'. \n\n \
                        For running the algorithm (with default parameters) on a test-set with 100 random genomes of length 25, type 't'  \n\n")

    if default == 'd':
        print(populationBased(300, data.mel, data.mir))

    if default == 'c':
        print("\nDefine the population size you would like the algorithm to use.\n\n \
                For a population size of 50, type 'xs'.\n\n \
                For a population size of 150, type 's'\n\n \
                For a population size of 300, type 'm'.\n\n \
                For a population size of 500, type 'l'\n\n \
                For a population size of 1000, type 'xl'\n\n")
        print("TODO")

    if default == 't':
        tester.randomTester(populationBased)
    #
    # else:
    #     print("Error, unknown input")


''' SIMULATED ANNEALING '''
if algorithm == '3':

    default = input("\n If you want to run the algorithm once with the default parameters, type 'd'.\n\n \
                        For custom parameters, type 'c'. \n\n \
                        For running the algorithm (with default parameters) on a test-set with 100 random genomes of length 25, type 't'  \n\n")

    if default == 'd':
        print(simulatedAnnealing(data.mel, data.mir, 1000, score.scoreNeighbours))

    elif default == 'c':

        print("\nDefine the score-function you would like to use.\n\nFor scoreNeighbours, type: 1\nFor scoreNeighboursModifier, type: 2\n")
        scoreF = input("Type in which score-funtion that you would like the algorithm to use: ")

        if scoreF == '1':
            print("\nDefine the interval with which the algorithm allows lesser mutations to pass.\n\nFor an interval of 1000, type: s\nFor an interval of 10.000, type: m\nFor an interval of 100.000, type l\n")
            failV = input("Type in which interval-size you would like the algorithm to use: ")

            if failV == 's':
                print(simulatedAnnealing(data.mel, data.mir, 1000, score.scoreNeighbours))
            if failV == 'm':
                print(simulatedAnnealing(data.mel, data.mir, 10000, score.scoreNeighbours))
            if failV == 'l':
                print(simulatedAnnealing(data.mel, data.mir, 100000, score.scoreNeighbours))

        elif scoreF == '2':
            print("\nDefine the interval with which the algorithm allows lesser mutations to pass.\n\nFor an interval of 1000, type: s\nFor an interval of 10.000, type: m\nFor an interval of 100.000, type l\n")
            failV = input("Type in which interval-size you would like the algorithm to use: ")

            if failV == 's':
                print(simulatedAnnealing(data.mel, data.mir, 1000, score.scoreNeighboursModifier))
            if failV == 'm':
                print(simulatedAnnealing(data.mel, data.mir, 10000, score.scoreNeighboursModifier))
            if failV == 'l':
                print(simulatedAnnealing(data.mel, data.mir, 100000, score.scoreNeighboursModifier))
        else:
            print("Error, unknown input")

    elif default == 't':
        tester.simulatedAnnealing()

    # else:
    #     print("Error, unknown input")

''' STEEPEST DESCEND VALLEY ABSEILER '''
if algorithm == '4':
    print(steepestDescendValleyAbseiler(data.mir, data.mel))
#
# else:
#     print("Error, unknown input")
