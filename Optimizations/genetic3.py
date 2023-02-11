
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
        for j in range(10):
            movesA = solutions[i]
            testList = [1,2,5,7,8]
            sim.simulate(strategyA= 15, strategyB= random.choice(testList))
            results[i] += sim.getCurrentScoreA()
    
    return results

def getGenetic4Move_A(round, logFile):
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




def getGenetic4Move_B(round, logFile):
    return 0
    # test = readLast_n_Lines(1, logFile)
    # print(round)
    
    # if(test[0] == "0"): return movesA[round][0]

    # return movesA[round][1]




def fitness(result):
    return -(result/10)

# Values for 3 memory:
#         0,1
#   0,1        0,1
# 0,1 0,1    0,1  0,1

# For 2 levels:
# [00, 01, 10, 11]
# For 3 Levels:
# [000, 001, 010, 011, 100, 101, 110, 111]

def getValue(bestSolutions, solNum, round, k):
    p = 0.7
    if(round == 0):
        if(random.random() < p):
            return bestSolutions[solNum][1][0]
        else:
            return bestSolutions[random.randint(0, 31)][1][0]
            
    if(random.random() < p):
        return bestSolutions[solNum][1][round][k]
    else:
        return bestSolutions[random.randint(0, 31)][1][round][k]


def startGeneticv4(sim):
    #Possible characters
    solutions = []
    #Putting all possibilities in list
    for _ in range(64):
        temp = []
        temp.append(random.randint(0,1))
        temp.append([random.randint(0,1), random.randint(0,1)])
        temp.append([random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])

        for i in range(3, 10):
            temp.append([random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])
        solutions.append(temp)
    

    for i in range(200):
        results = compete(solutions, sim)

        rankedSolutions = []
        for j in range(len(solutions)):
            rankedSolutions.append((fitness(results[j]), solutions[j]))
        
        rankedSolutions.sort()
        rankedSolutions.reverse()

        print(f"=== Gen {i} best solution ===")

        for o in range(10):
            print(rankedSolutions[o][0])
        
        if(i == 199):
            with open("Results/genetic4.json", 'w') as file_object:  #open the file in write mode
                json.dump(rankedSolutions[0][1], file_object)
            break
        bestSolutions = rankedSolutions[:32]

        newGen = []
        # * random.uniform(0.99, 1.01) will mutate by 2%
        for i in range(32):
            temp = [getValue(bestSolutions, i,0,0), 
                    [getValue(bestSolutions, i,1,0),getValue(bestSolutions, i,1,1)], 
                    [getValue(bestSolutions, i,2,0),getValue(bestSolutions, i,2,1),getValue(bestSolutions, i,2,2),getValue(bestSolutions, i,2,3)]]

            for j in range(3, 10):
                temp.append([getValue(bestSolutions, i,j,0),
                            getValue(bestSolutions, i,j,1),
                            getValue(bestSolutions, i,j,2),
                            getValue(bestSolutions, i,j,3),
                            getValue(bestSolutions, i,j,4),
                            getValue(bestSolutions, i,j,5),
                            getValue(bestSolutions, i,j,6),
                            getValue(bestSolutions, i,j,7)
                            ])
            
            newGen.append(temp)

            temp = [getValue(bestSolutions, i,0,0), 
                    [getValue(bestSolutions, i,1,0),getValue(bestSolutions, i,1,1)], 
                    [getValue(bestSolutions, i,2,0),getValue(bestSolutions, i,2,1),getValue(bestSolutions, i,2,2),getValue(bestSolutions, i,2,3)]]

            for j in range(3,10):
                temp.append([getValue(bestSolutions, i,j,0),
                            getValue(bestSolutions, i,j,1),
                            getValue(bestSolutions, i,j,2),
                            getValue(bestSolutions, i,j,3),
                            getValue(bestSolutions, i,j,4),
                            getValue(bestSolutions, i,j,5),
                            getValue(bestSolutions, i,j,6),
                            getValue(bestSolutions, i,j,7)
                            ])

            newGen.append(temp)

        solutions = newGen



# startGenetic(1)
