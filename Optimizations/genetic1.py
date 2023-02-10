
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
        for j in range(10):
            movesA = solutions[i]
            testList = [1,2,5,7,8]
            sim.simulate(strategyA= 12, strategyB= random.choice(testList))
            results[i] += sim.getCurrentScoreA()
    
    return results

def getGeneticMove_A(round):
    return movesA[round]

def getGeneticMove_B(round):
    return movesB[round]



def fitness(result):
    return -(result/10)


def startGeneticv1(sim):
    #Possible characters

    #Putting all possibilities in list
    solutions = []

    for _ in range(64):
        solutions.append([random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])


    for i in range(50):
        results = compete(solutions, sim)

        rankedSolutions = []
        for j in range(len(solutions)):
            rankedSolutions.append((fitness(results[j]), solutions[j]))
        
        rankedSolutions.sort()
        rankedSolutions.reverse()

        print(f"=== Gen {i} best solution ===")
        print(rankedSolutions[0])

        if(i == 49):
            with open("Results/genetic1.json", 'w') as file_object:  #open the file in write mode
                json.dump(rankedSolutions[0][1], file_object)
            break

        bestSolutions = rankedSolutions[:32]

        newGen = []
        p = 0.7
        # * random.uniform(0.99, 1.01) will mutate by 2%
        for i in range(32):
            temp = [0,0,0,0,0,0]
            for j in range(0, 6):
                if(random.random() < p):
                    temp[j] = bestSolutions[i][1][j]
                else:
                    temp[j] = bestSolutions[random.randint(0, 31)][1][j] 
            
            newGen.append(temp)

            for j in range(0, 6):
                if(random.random() < p):
                    temp[j] = bestSolutions[i][1][j]
                else:
                    temp[j] = bestSolutions[random.randint(0, 31)][1][j] 
            
            newGen.append(temp)

            
        
        solutions = newGen
