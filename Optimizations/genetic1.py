
'''
6 ROUNDS 

MINMIZE SCORE TO 0

All genetic offsprings compete with each other

Start with combinations of 1's and 0's

OBSERVATION:
- We are getting all 0 (every best solution is all 0's)


PROBLEM
1. Algorithm does not choose based on what was seen before (just spits out values)
2. They are just choosing to cooperate

'''
import itertools
import random
import json


movesA = []
movesB = []


# def compete(solutions, sim):
#     global movesA
#     global movesB
#     results = [0] *  len(solutions)
#     for i in range(len(solutions)):
#         for j in range(len(solutions)):
#             if(i != j):
#                 movesA = solutions[i]
#                 movesB = solutions[j]
#                 sim.simulate(strategyA= 12, strategyB= 12)
#                 results[i] += sim.getCurrentScoreA()
    
#     return results

def compete(solutions, sim):
    global movesA
    global movesB
    results = [0] *  len(solutions)
    for i in range(len(solutions)):
        for j in [1,2,4,5,6,7,8,9,10]:
            movesA = solutions[i]
            sim.simulate(strategyA= 12, strategyB= j)
            results[i] += sim.getCurrentScoreA()
    
    return results

def getGeneticMove_A(round):
    return movesA[round]

def getGeneticMove_B(round):
    return movesB[round]



def fitness(result):
    return result/9



def startGeneticv1(sim, popSize):
    #Possible characters

    #Putting all possibilities in list
    solutions = []
    lowestScore = []
    avgScore = []

    for _ in range(popSize):
        solutions.append([random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])


    for i in range(100):
        results = compete(solutions, sim)

        rankedSolutions = []
        for j in range(len(solutions)):
            rankedSolutions.append((fitness(results[j]), solutions[j]))
        
        rankedSolutions.sort()
        # rankedSolutions.reverse()

        print(f"=== Gen {i} best solution ===")
        print(rankedSolutions[0])


        temp = 0
        for _ in range(popSize):
            temp += rankedSolutions[0][0]
        
        temp = temp / popSize
        avgScore.append(temp)

        lowestScore.append(rankedSolutions[0][0])


        if(i == 99):
            with open("Results/GeneticData_PopulationTest/genetic1_pop" + str(popSize) + ".json", 'w') as file_object:  #open the file in write mode
                json.dump(rankedSolutions[0][1], file_object)
            break

        bestSolutions = rankedSolutions[:(popSize//2)]

        newGen = []
        p = 0.7
        # * random.uniform(0.99, 1.01) will mutate by 2%
        for i in range((popSize//2)):
            temp = [0] * 10
            for j in range(0, 10):
                if(random.random() < p):
                    temp[j] = bestSolutions[i][1][j]
                else:
                    temp[j] = bestSolutions[random.randint(0, (popSize//2)-1)][1][j] 
            
            newGen.append(temp)

            for j in range(0, 10):
                if(random.random() < p):
                    temp[j] = bestSolutions[i][1][j]
                else:
                    temp[j] = bestSolutions[random.randint(0, (popSize//2)-1)][1][j] 
            
            newGen.append(temp)

            
        
        solutions = newGen


    with open("Results/GeneticData_PopulationTest/genetic1_scores_" + str(popSize) + ".json", 'w') as file_object:  #open the file in write mode
        json.dump(lowestScore, file_object)
    with open("Results/GeneticData_PopulationTest/genetic1_scores_averages_" + str(popSize) + ".json", 'w') as file_object:  #open the file in write mode
        json.dump(avgScore, file_object)