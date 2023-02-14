
import itertools
import random
import os
import json


movesA = []

def readLast_n_Lines(n, fileName):
    if(not os.path.isfile(fileName) or os.stat(fileName).st_size == 0): return None

    with open(fileName, "r") as file:
        return file.readlines()[-n:]


def compete(solutions, sim):
    global movesA
    global movesB
    results = [0] *  len(solutions)
    for i in range(len(solutions)):
        for j in [1,2,4,5,7,8,9]:
            movesA = solutions[i]
            sim.simulate(strategyA= 15, strategyB= j)
            results[i] += sim.getCurrentScoreA()
    
    return results

def getGenetic3Move_A(round, logFile):
    if(round == 0): return movesA[0]

    if(round == 1):
        test = readLast_n_Lines(1, logFile)
        if(test[0][2] == "0"): return movesA[round][0]
        return movesA[round][1]
    
    if(round == 2):
        test = readLast_n_Lines(2, logFile)
        if(test[1][2] == "0"):
            if(test[0][2] == "0"):
                return movesA[round][0] 
            return movesA[round][1] 
        else:
            if(test[0][2] == "0"):
                return movesA[round][2] 
            return movesA[round][3] 

    else:
        test = readLast_n_Lines(3, logFile)
        if(test[2][2] == "0"):
            if(test[1][2] == "0"):
                if(test[0][2] == "0"):
                    return movesA[round][0] 
                return movesA[round][1] 
            else:
                if(test[0][2] == "0"):
                    return movesA[round][2] 
                return movesA[round][3] 
        else:
            if(test[1][2] == "0"):
                if(test[0][2] == "0"):
                    return movesA[round][4] 
                return movesA[round][5] 
            else:
                if(test[0][2] == "0"):
                    return movesA[round][6] 
                return movesA[round][7] 




def getGenetic3Move_B(round, logFile):
    return 0
    # test = readLast_n_Lines(1, logFile)
    # print(round)
    
    # if(test[0] == "0"): return movesA[round][0]

    # return movesA[round][1]




def fitness(result):
    return result/8.75

# Values for 3 memory:
#         0,1
#   0,1        0,1
# 0,1 0,1    0,1  0,1

# For 2 levels:
# [00, 01, 10, 11]
# For 3 Levels:
# [000, 001, 010, 011, 100, 101, 110, 111]

def getValue(bestSolutions, solNum, round, k, popSize, crossoverP):
    mut = 0.001
    val = 0
    if(round == 0):
        if(random.random() < crossoverP):
            val = bestSolutions[solNum][1][0]
        else:
            val = bestSolutions[random.randint(0, (popSize//2)-1)][1][0]   
    elif(random.random() < crossoverP):
        val = bestSolutions[solNum][1][round][k]
    else:
        val = bestSolutions[random.randint(0, (popSize//2)-1)][1][round][k]

    if(random.random() < mut):
        if(val == 1): return 0
        if(val == 0): return 1
    else:
        return val


def startGeneticv3(sim, popSize, crossoverP):
    #Possible characters
    solutions = []
    lowestScore = []
    avgScore = []
    #Putting all possibilities in list
    for _ in range(popSize):
        temp = []
        temp.append(random.randint(0,1))
        temp.append([random.randint(0,1), random.randint(0,1)])
        temp.append([random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])

        for _ in range(3, 10):
            temp.append([random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])
        solutions.append(temp)
    

    for i in range(100):
        results = compete(solutions, sim)

        rankedSolutions = []
        for j in range(len(solutions)):
            rankedSolutions.append((fitness(results[j]), solutions[j]))
        
        rankedSolutions.sort()
        # rankedSolutions.reverse()

        print(f"=== Gen {i} best solution ===")

        for o in range(3):
            print(rankedSolutions[o][0])

        temp = 0
        for _ in range(popSize):
            temp += rankedSolutions[0][0]
        
        temp = temp / popSize
        avgScore.append(temp)
        
        lowestScore.append(rankedSolutions[0][0])
        
        if(i == 99):
            with open("Results/GeneticData_Crossover/genetic3_pop" + str(crossoverP) + ".json", 'w') as file_object:  #open the file in write mode
                json.dump(rankedSolutions[0][1], file_object)
            break
        bestSolutions = rankedSolutions[:(popSize//2)]

        newGen = []
        # * random.uniform(0.99, 1.01) will mutate by 2%
        for i in range((popSize//2)):
            temp = [getValue(bestSolutions, i,0,0, popSize, crossoverP), 
                    [getValue(bestSolutions, i,1,0, popSize, crossoverP),getValue(bestSolutions, i,1,1, popSize, crossoverP)], 
                    [getValue(bestSolutions, i,2,0, popSize, crossoverP),getValue(bestSolutions, i,2,1, popSize, crossoverP),getValue(bestSolutions, i,2,2, popSize, crossoverP),getValue(bestSolutions, i,2,3, popSize, crossoverP)]]

            for j in range(3, 10):
                temp.append([getValue(bestSolutions, i,j,0, popSize, crossoverP),
                            getValue(bestSolutions, i,j,1, popSize, crossoverP),
                            getValue(bestSolutions, i,j,2, popSize, crossoverP),
                            getValue(bestSolutions, i,j,3, popSize, crossoverP),
                            getValue(bestSolutions, i,j,4, popSize, crossoverP),
                            getValue(bestSolutions, i,j,5, popSize, crossoverP),
                            getValue(bestSolutions, i,j,6, popSize, crossoverP),
                            getValue(bestSolutions, i,j,7, popSize, crossoverP)
                            ])
            
            newGen.append(temp)

            temp = [getValue(bestSolutions, i,0,0, popSize, crossoverP), 
                    [getValue(bestSolutions, i,1,0, popSize, crossoverP),getValue(bestSolutions, i,1,1, popSize, crossoverP)], 
                    [getValue(bestSolutions, i,2,0, popSize, crossoverP),getValue(bestSolutions, i,2,1, popSize, crossoverP),getValue(bestSolutions, i,2,2, popSize, crossoverP),getValue(bestSolutions, i,2,3, popSize, crossoverP)]]

            for j in range(3,10):
                temp.append([getValue(bestSolutions, i,j,0, popSize, crossoverP),
                            getValue(bestSolutions, i,j,1, popSize, crossoverP),
                            getValue(bestSolutions, i,j,2, popSize, crossoverP),
                            getValue(bestSolutions, i,j,3, popSize, crossoverP),
                            getValue(bestSolutions, i,j,4, popSize, crossoverP),
                            getValue(bestSolutions, i,j,5, popSize, crossoverP),
                            getValue(bestSolutions, i,j,6, popSize, crossoverP),
                            getValue(bestSolutions, i,j,7, popSize, crossoverP)
                            ])

            newGen.append(temp)

        solutions = newGen


    with open("Results/GeneticData_Crossover/genetic3_scores_" + str(crossoverP) + ".json", 'w') as file_object:  #open the file in write mode
        json.dump(lowestScore, file_object)
    with open("Results/GeneticData_Crossover/genetic3_scores_averages_" + str(crossoverP) + ".json", 'w') as file_object:  #open the file in write mode
        json.dump(avgScore, file_object)

# startGenetic(1)

