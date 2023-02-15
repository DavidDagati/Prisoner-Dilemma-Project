
import itertools
import random
import os
import json


movesA = []

def readLast_n_Lines(n, fileName):
    if(not os.path.isfile(fileName) or os.stat(fileName).st_size == 0): return None

    with open(fileName, "r") as file:
        return file.readlines()[-n:]

# All generations will compete against the training set 
def compete(solutions, sim):
    global movesA
    global movesB
    results = [0] *  len(solutions)
    for i in range(len(solutions)):
        for j in [1,2,4,5,7,8,9,10]:
            movesA = solutions[i]
            sim.simulate(strategyA= 15, strategyB= j)
            results[i] += sim.getCurrentScoreA()
    
    return results

# Gets the array element for the move
def getGenetic3Move_A(round, logFile):
    # Only one option in round 1:
    if(round == 0): return movesA[0]

    # Two Options in round 2
    if(round == 1):
        test = readLast_n_Lines(1, logFile)
        if(test[0][2] == "0"): return movesA[round][0]
        return movesA[round][1]
    
    # Four Options in round 3
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
    
    # Eight Options in remaining rounds
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





def fitness(result):
    return result/8



def getValue(bestSolutions, solNum, round, k, popSize, crossoverP, mut):
    val = 0
    # Special case for round 1:
    if(round == 0):
        if(random.random() < crossoverP):
            val = bestSolutions[solNum][1][0]
        else:
            val = bestSolutions[random.randint(0, (popSize//2)-1)][1][0]   
    # Perform crossover:
    elif(random.random() < crossoverP):
        val = bestSolutions[solNum][1][round][k]
    else:
        val = bestSolutions[random.randint(0, (popSize//2)-1)][1][round][k]

    # Perform Mutation:
    if(random.random() < mut):
        if(val == 1): return 0
        if(val == 0): return 1
    else:
        return val


def startGeneticv3(sim, popSize, crossoverP, mut, folder="Default"):
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

        print(f"=== Gen {i} top 3 scores ===")

        for o in range(3):
            print(rankedSolutions[o][0])

        # Calculate average score
        temp = 0
        for _ in range(popSize):
            temp += rankedSolutions[0][0]
        
        temp = temp / popSize
        avgScore.append(temp)
        
        # Add lowest score
        lowestScore.append(rankedSolutions[0][0])
        
        # Dump final solution when complete
        if(i == 99):
            with open(f"Results/{folder}/genetic3_mut{mut}_pop{popSize}_crP{crossoverP}.json", 'w') as file_object:  #open the file in write mode
                json.dump(rankedSolutions[0][1], file_object)
            break
        bestSolutions = rankedSolutions[:(popSize//2)]

        newGen = []
        # Generate 64 New Solutions
        for i in range((popSize//2)):
            # Generate First three rounds:
            temp = [getValue(bestSolutions, i,0,0, popSize, crossoverP, mut), 
                    [getValue(bestSolutions, i,1,0, popSize, crossoverP, mut),getValue(bestSolutions, i,1,1, popSize, crossoverP, mut)], 
                    [getValue(bestSolutions, i,2,0, popSize, crossoverP, mut),getValue(bestSolutions, i,2,1, popSize, crossoverP, mut),getValue(bestSolutions, i,2,2, popSize, crossoverP, mut),getValue(bestSolutions, i,2,3, popSize, crossoverP, mut)]]

            # Generate remaining rounds:
            for j in range(3, 10):
                temp.append([getValue(bestSolutions, i,j,0, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,1, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,2, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,3, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,4, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,5, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,6, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,7, popSize, crossoverP, mut)
                            ])
            
            newGen.append(temp)

            # Generate First three rounds:
            temp = [getValue(bestSolutions, i,0,0, popSize, crossoverP, mut), 
                    [getValue(bestSolutions, i,1,0, popSize, crossoverP, mut),getValue(bestSolutions, i,1,1, popSize, crossoverP, mut)], 
                    [getValue(bestSolutions, i,2,0, popSize, crossoverP, mut),getValue(bestSolutions, i,2,1, popSize, crossoverP, mut),getValue(bestSolutions, i,2,2, popSize, crossoverP, mut),getValue(bestSolutions, i,2,3, popSize, crossoverP, mut)]]

            # Generate remaining rounds:
            for j in range(3,10):
                temp.append([getValue(bestSolutions, i,j,0, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,1, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,2, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,3, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,4, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,5, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,6, popSize, crossoverP, mut),
                            getValue(bestSolutions, i,j,7, popSize, crossoverP, mut)
                            ])

            newGen.append(temp)

        solutions = newGen


    with open(f"Results/{folder}/genetic3_SCORES_mut{mut}_pop{popSize}_crP{crossoverP}.json", 'w') as file_object:  #open the file in write mode
        json.dump(lowestScore, file_object)
    with open(f"Results/{folder}/genetic3_SCOREAVERAGES_mut{mut}_pop{popSize}_crP{crossoverP}.json" + str(crossoverP) + ".json", 'w') as file_object:  #open the file in write mode
        json.dump(avgScore, file_object)

