
import itertools
import random
import os
import json


movesA = []

def readLastLine(fileName):
    if(not os.path.isfile(fileName) or os.stat(fileName).st_size == 0): return None

    with open(fileName, "r") as file:
        return file.readlines()[-1]


def compete(solutions, sim):
    global movesA
    global movesB
    results = [0] *  len(solutions)
    for i in range(len(solutions)):
        for j in range(10):
            movesA = solutions[i]
            testList = [1,2,5,7,8]
            sim.simulate(strategyA= 14, strategyB= random.choice(testList))
            results[i] += sim.getCurrentScoreA()
    
    return results




def getGenetic3Move_A(round, logFile):
    test = readLastLine(logFile)
    if(round == 0): return movesA[0]

    if(test[2] == "0"): movesA[round][0]

    return movesA[round][1]

def getGenetic3Move_B(round, logFile):
    test = readLastLine(logFile)
    print(round)
    
    if(test[0] == "0"): return movesA[round][0]

    return movesA[round][1]




def fitness(result):
    return -(result/10)


def startGeneticv3(sim):
    #Possible characters

    #Putting all possibilities in list
    solutions = []
    for _ in range(64):
        temp = []
        temp.append(random.randint(0,1))
        for i in range(1, 10):
            temp.append([random.randint(0,1), random.randint(0,1)])
        solutions.append(temp)
            

    for i in range(200):
        results = compete(solutions, sim)

        rankedSolutions = []
        for j in range(len(solutions)):
            rankedSolutions.append((fitness(results[j]), solutions[j]))
        
        rankedSolutions.sort()
        rankedSolutions.reverse()

        print(f"=== Gen {i} best solution ===")

        for o in range(3):
            print(rankedSolutions[o])
    
        if(i == 199):
            with open("Results/genetic3.json", 'w') as file_object:  #open the file in write mode
                json.dump(rankedSolutions[0][1], file_object)
            break
        
    
        bestSolutions = rankedSolutions[:32]

        newGen = []
        p = 0.7
        # * random.uniform(0.99, 1.01) will mutate by 2%
        for i in range(32):
            temp = [0, [0,0], [0,0],[0,0],[0,0],[0,0], [0,0], [0,0], [0,0], [0,0]]
            
            if(random.random() < p): 
                temp[0] = bestSolutions[i][1][0] # 70% of this
            else:
                temp[0] = bestSolutions[random.randint(0, 31)][1][0]  # 30% of this
                
            for j in range(1, len(temp)):
                if(random.random() < p):
                    temp[j][0] = bestSolutions[i][1][j][0]
                else:
                    temp[j][0] = bestSolutions[random.randint(0, 31)][1][j][0]
                
                if(random.random() < p):
                    temp[j][1] = bestSolutions[i][1][j][1]
                else:
                    temp[j][1] = bestSolutions[random.randint(0, 31)][1][j][1]
            
            newGen.append(temp)

            
            if(random.random() < p):
                temp[0] = bestSolutions[i][1][0]
            else:
                temp[0] = bestSolutions[random.randint(0, 31)][1][0] 
                

            for j in range(1, len(temp)):
                if(random.random() < p):
                    temp[j][0] = bestSolutions[i][1][j][0]
                else:
                    temp[j][0] = bestSolutions[random.randint(0, 31)][1][j][0]
                
                if(random.random() < p):
                    temp[j][1] = bestSolutions[i][1][j][1]
                else:
                    temp[j][1] = bestSolutions[random.randint(0, 31)][1][j][1]

            newGen.append(temp)

        solutions = newGen
