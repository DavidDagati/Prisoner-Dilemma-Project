import numpy as np
from collections import Counter
import json

import sys
sys.path.append('../Strategies')
from allCooperate import allCooperate 
from allDefects import allDefects
from random_strat import random
from everyOther import everyOther
from adaptivePavlov import adaptivePavlov
from pavlov import pavlov
from TicForTac import titForTat_B
from suspiciousTitForTat import suspiciousTitForTat
from titForTwoTats import titForTwoTats
from grim import grim

global SIZE
SIZE = 10

def playRound(moveA, moveB) -> tuple[int,int]:
        if moveA == 0: 
            if moveB == 0:
                # Both Cooperate
                return (-1, -1)
            else:
                # A Cooperates, B Deflects 
                return (-20, 0)
            
        if moveA == 1:
            if moveB == 0:
                # A Deflects, B Cooperates
                return (0, -20)
            else:
                # Both Deflect
                return (-10, -10)
        
        # If error occurs:
        return None

def compete(arr):
    moveA = 0
    moveB = 0
    totalScoreA = 0
    totalScoreB = 0
    winsA = 0
    logFileName = '../Results/HillClimbing/hillClimbing.txt'
    strategies = {0:"allCooperate()", 1:"allDefects(logFileName, 1)", 2:"random(logFileName, 1)", 3: "everyOther(j)", 4: "pavlov(logFileName, 1)", 5:"adaptivePavlov(logFileName, 1)", 6:"titForTat_B(logFileName)", 7: "suspiciousTitForTat(logFileName, 1)", 8:"titForTwoTats(logFileName, 'B')", 9:"grim(logFileName, 'B')"}

    #print("Length=", len(strategies))
    
    
    # Loop through all the rounds
    for i in range(len(strategies)):
        scoreA = 0
        scoreB = 0
        
        # Clear the File
        file = open(logFileName, "w")
        file.close()

        for j in range(SIZE):
            
            # Find strategy for A:
            moveA = arr[j]
            # Find Strategy for B:
            moveB = eval(strategies[i])
            # if (i == 9):
            #     print("moveA: ", moveA, " ", strategies[i], ": ", moveB)
            # else:
            #     pass

            # Update log.txt:
            file = open(logFileName, "a")
            file.write(f"{moveA} {moveB}\n")
            file.close()

            # Update Total Score for Player A and B
            scores = playRound(moveA, moveB)
            scoreA += scores[0]
            scoreB += scores[1]
            totalScoreA += scores[0]
            totalScoreB += scores[1]
            
        if (scoreA >= scoreB):
            winsA += 1
            
        #print (scoreA)
    #return totalScoreA
    return winsA



def HillClimbing():
    scoreArray1 = scoreArray2 = 0
    #print("Start: ", adaptivePavlov('../Results/hillClimbing.txt', 1))
    Array1 = np.random.randint(0,2,SIZE)
    
    scoreArray1 = compete(Array1)
    #print("Initial Array: ", Array1, scoreArray1, "\n")
    
    for i in range(50): # Iteration
        for i in range(SIZE): #size of array
            Array2 = np.array(Array1)
            Array2[i] = 1 if Array1[i] == 0 else 0
            scoreArray2 = compete(Array2)
            
            if (scoreArray2 > scoreArray1):
                Array1 = np.array(Array2)
                scoreArray1 = scoreArray2
            
            #print("New Array: ", Array2, scoreArray2)
        
    #print("Winner:", Array1, " ", scoreArray1)
    return(Array1, scoreArray1)

        
    
    
totalWinners = []    
for k in range(100):
    winner, score = HillClimbing()
    winner = " ".join(str(e) for e in winner)
    totalWinners.append(winner)
    
dictTotalWinners = list(Counter(totalWinners).keys())
dictTotalWins = list(Counter(totalWinners).values())

print(totalWinners)
print(dictTotalWinners) 
print(dictTotalWins) 

# Putting into json files
# json_totalWinners = json.dumps(dictTotalWinners)
# json_totalWins = json.dumps(dictTotalWins)

# file = open('../Results/HillClimbing/ByWinSize10Iteration50Winners.json', "w")
# file.write(json_totalWinners)
# file.close()

# file = open('../Results/HillClimbing/ByWinSize10Iteration50Wins.json', "w")
# file.write(json_totalWins)
# file.close()