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
from visualizations import visualize

<<<<<<< HEAD
algorithm = input("\n   WELCOME!\n\n"
    + "|--------------------------------------------------------------------"
    + "-------------------|\n"
    + "\n| When you want to run the pancake sorting algorithm type in: 1"
    + "                         |"
    + "\n\n| When you want to run the population based algorithm type in: 2"
    + "                        |"
    + "\n\n| When you want to run the simulated annealing algorithm type in: 3"
    + "                     |"
    + "\n\n| When you want to run the Steepest Descend Valley Abseiler"
    + " algorithm, type in: 4       |\n\n"
    + "|--------------------------------------------------------------------"
    + "-------------------|\n"
    + "\n\nType in the algorithm that you want to run: ")

=======
print("\nWELCOME!"
    + "\n\n When you want to run the pancake sorting algorithm type in: 1"
    + "\n\n When you want to run the population based algorithm type in: 2"
    + "\n\n When you want to run the simulated annealing algorithm type in: 3"
    + "\n\n When you want to run the Steepest Descend Valley Abseiler algorithm"
    + ", type in: 4\n\n For direct result visualization type in: 5 \n")
>>>>>>> bc8635b453666c055d292adeb4168f958131935f


''' PANCAKESORT '''
if algorithm == '1':
    default = input("|-------------------------------------------------------"
                  + "---------------------------------|\n"
                  + "\n| If you want to run the algorithm with default"
                  + "parameters, type 'd'                      |\n\n"
                  + "| For running the algorithm on a test-set with 100 random "
                  + "genomes of length 25, type 't' |\n\n"
                  + "|-------------------------------------------------------"
                  + "---------------------------------|\n\n"
                  + "\n\nType in how you want to run the algorithm: ")

    if default == 'd':
        print(pancakeSort(data.mel, data.mir))
<<<<<<< HEAD

    elif default == 't':
        tester.pancakeTester()

''' POPULATION BASED '''
if algorithm == '2':
    default = input("|-------------------------------------------------------"
                  + "---------------------------------|\n"
                  + "\n| If you want to run the algorithm once with the default"
                  + " parameters, type 'd'            |\n\n"
                  + "| For custom parameters, type 'c'                       "
                  + "                                 |\n\n"
                  + "| For running the algorithm (with default parameters)"
                  + " on a test-set with 100 random      |\n"
                  + "| genomes of length 25, type 't'                        "
                  + "                                 |\n\n"
                  + "| For running the algorithm on a test-set"
                  + " with visualisation, type 'v'                   |\n\n"
                  + "|-------------------------------------------------------"
                  + "---------------------------------|\n\n"
                  + "\n\nType in how you want to run the algorithm: ")
=======
    if default == 't':
        tester.pancakeTester([*range(1,26)])
        # visualize.simulatedVisualizer()
        #visualize.populationVisualizer

''' POPULATION BASED '''
if algorithm == '2':
    default = input("\n If you want to run the algorithm once with the default"
                  + " parameters, type 'd'.\n\n For custom parameters, type 'c'"
                  + " \n\n For running the algorithm (with default parameters)"
                  + " on a test-set with 100 random genomes of length 25,"
                  + " type 't'\n\n For running the algorithm on a test-set"
                  + " with visualisation, type 'tv' \n\n For running the"
                  + " algorithm 100 times with default parameters, type 'dt'"
                  + " \n\n For running the algorithm 100 times with different"
                  + " parameters with visualization, type 'dv' \n\n")
>>>>>>> bc8635b453666c055d292adeb4168f958131935f

    if default == 'd':
        print(populationBased(150, data.mel, data.mir))

    elif default == 'c':
        popSize = input("|----------------------------------------------------"
                      + "------------------------------------|\n"
                      + "\n| Define the population size you would like the "
                      + "algorithm to use.                        |\n\n"
                      + "| For a population size of 50, type 's' "
                      + "                                                 |\n\n"
                      + "| For a population size of 150, type 'm' "
                      + "                                                |\n\n"
                      + "| For a population size of 300, type 'l' "
                      + "                                                |\n\n"
                      + "| For a population size of 500, type 'xl' "
                      + "                                               |\n\n"
                      + "|----------------------------------------------------"
                      + "------------------------------------|\n\n"
                      + "Type in which population-size you would like the"
                      + " algorithm to use: ")

        if popSize == 's':
            print(populationBased(50, data.mel, data.mir))

        elif popSize == 'm':
            print(populationBased(150, data.mel, data.mir))

        elif popSize == 'l':
            print(populationBased(300, data.mel, data.mir))

        elif popSize == 'xl':
            print(populationBased(500, data.mel, data.mir))

<<<<<<< HEAD
    elif default == 't':
        tester.populationTester(150)
    #
    # else:
    #     print("Error, unknown input")
    elif default == 'v':
        visualize.populationVisualizer()
=======
    if default == 't':
        tester.populationTester(150, [*range(1,26)])

    #visualize.populationVisualizer()
    # else:
    #     print("Error, unknown input")
    if default == 'tv':
        visualize.populationVisualizer([*range(1,26)])

    if default == 'dt':
        tester.populationTester(150, data.mel)

    if default == 'dv':
        visualize.populationVisualizer(data.mel)
>>>>>>> bc8635b453666c055d292adeb4168f958131935f

''' SIMULATED ANNEALING '''
if algorithm == '3':
    default = input("|-------------------------------------------------------"
                  + "---------------------------------|\n"
                  + "\n| If you want to run the algorithm once with the default"
                  + " parameters, type 'd'            |\n\n"
                  + "| For custom parameters, type 'c'                       "
                  + "                                 |\n\n"
                  + "| For running the algorithm (with default parameters)"
                  + " on a test-set with 100 random      |\n"
                  + "| genomes of length 25, type 't'                        "
                  + "                                 |\n\n"
                  + "| For running the algorithm on a test-set"
                  + " with visualisation, type 'v'                   |\n\n"
                  + "|-------------------------------------------------------"
                  + "---------------------------------|\n\n"
                  + "\n\nType in how you want to run the algorithm: ")

    if default == 'd':
        print(simulatedAnnealing(data.mel, data.mir, 1000,
                                 score.scoreNeighbours))

    elif default == 'c':

        scoreF = input("|-------------------------------------------------"
                     + "---------------------------------------|\n"
                     + "\n| Define the score-function you would like to use."
                     + "                                       |\n\n"
                     + "| For scoreNeighbours, type: 1                    "
                     + "                                       |\n\n"
                     + "| For scoreNeighboursModifier, type: 2            "
                     + "                                       |\n\n"
                     + "|-------------------------------------------------"
                     + "---------------------------------------|\n\n"
                     + " Type in which score-function you would like the"
                     + " algorithm to use: ")

        if scoreF == '1':
            failV = input("|-------------------------------------------------"
                        + "---------------------------------------|\n"
                        + "\n| Define the interval with which the algorithm"
                        + " allows lesser mutations to pass.          |\n\n"
                        + "| For an interval of 1000, type: s             "
                        + "                                          |\n\n"
                        + "| For an interval of 10.000, type: m           "
                        + "                                          |\n\n"
                        + "| For an interval of 100.000, type l           "
                        + "                                          |\n\n"
                        + "|-------------------------------------------------"
                        + "---------------------------------------|\n\n"
                        + "Type in which interval-size you would like the"
                        + " algorithm to use: ")

            if failV == 's':
                print(simulatedAnnealing(data.mel, data.mir, 1000,
                                         score.scoreNeighbours))
            elif failV == 'm':
                print(simulatedAnnealing(data.mel, data.mir, 10000,
                                         score.scoreNeighbours))
            elif failV == 'l':
                print(simulatedAnnealing(data.mel, data.mir, 100000,
                                         score.scoreNeighbours))
            else:
                print("Error, unknown input")

        elif scoreF == '2':
            failV = input("|-------------------------------------------------"
                        + "---------------------------------------|\n"
                        + "\n| Define the interval with which the algorithm"
                        + " allows lesser mutations to pass.          |\n\n"
                        + "| For an interval of 1000, type: s             "
                        + "                                          |\n\n"
                        + "| For an interval of 10.000, type: m           "
                        + "                                          |\n\n"
                        + "| For an interval of 100.000, type l           "
                        + "                                          |\n\n"
                        + "|-------------------------------------------------"
                        + "---------------------------------------|\n\n"
                        + "Type in which interval-size you would like the"
                        + " algorithm to use: ")

            if failV == 's':
                print(simulatedAnnealing(data.mel, data.mir, 1000,
                                         score.scoreNeighboursModifier))
            elif failV == 'm':
                print(simulatedAnnealing(data.mel, data.mir, 10000,
                                         score.scoreNeighboursModifier))
            elif failV == 'l':
                print(simulatedAnnealing(data.mel, data.mir, 100000,
                                         score.scoreNeighboursModifier))
            else:
                print("Error, unknown input")
        else:
            print("Error, unknown input")

    elif default == 't':
        tester.simulatedTester(1000, [*range(1,26)])


    elif default == 'v':
<<<<<<< HEAD
        visualize.simulatedVisualizer()
    else:
        print("Error, unknown input")
=======
        visualize.simulatedVisualizer([*range(1,26)])

>>>>>>> bc8635b453666c055d292adeb4168f958131935f

''' STEEPEST DESCEND VALLEY ABSEILER '''
if algorithm == '4':
    print(steepestDescendValleyAbseiler(data.mir, data.mel))
<<<<<<< HEAD





else:
    print("Error, unknown input")
=======
#
# else:
#     print("Error, unknown input")

if algorithm == '5':
    visualize.combinedVisualizer(data.mel, data.mir)
>>>>>>> bc8635b453666c055d292adeb4168f958131935f
