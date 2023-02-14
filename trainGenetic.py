
'''
Strategy Key:
0: UserInput (No Strategy)
1: Tic for Tat 
2: Pavlov 
3: Adaptive Pavlov 
4: Suspicious Tit for Tat 
5: Tit for Two Tats 
6: Random 
7: All cooperate 
8: All defect 
9: Every other 
10: GRIM 


--- 
11: Hill Climbing
12: Genetic Algorithm
13: 

To Run:
1. cd into main folder
2. run `python Simulator/main.py`

'''
from Strategies.userInput import userInput
from Strategies.TicForTac import titForTat_A, titForTat_B
from Strategies.pavlov import pavlov
from Strategies.adaptivePavlov import adaptivePavlov
from Strategies.suspiciousTitForTat import suspiciousTitForTat
from Strategies.titForTwoTats import titForTwoTats
from Strategies.random_strat import random
from Strategies.allCooperate import allCooperate
from Strategies.allDefects import allDefects
from Strategies.everyOther import everyOther
# from Strategies.grim import grim
# from Optimizations.hillClimbing import hillClimbing
from Optimizations.useGenetic import useGeneticV1
from Optimizations.useGenetic import useGeneticV2
from Optimizations.useGenetic import useGeneticV3


from Optimizations.genetic1 import getGeneticMove_A
from Optimizations.genetic1 import getGeneticMove_B
from Optimizations.genetic1 import startGeneticv1

from Optimizations.genetic2 import startGeneticv2
from Optimizations.genetic2 import getGenetic2Move_A
from Optimizations.genetic2 import getGenetic2Move_B


from Optimizations.genetic3 import startGeneticv3
from Optimizations.genetic3 import getGenetic3Move_A
from Optimizations.genetic3 import getGenetic3Move_B




class Simulator:
    def __init__(self, numOfRounds):
        self.numOfRounds = numOfRounds
        self.scoreA = 0
        self.scoreB = 0

        self.menu = {
 0: {"Name": "UserInput", 
                "FunctionA": "userInput(logFileName, 'A')", 
                "FunctionB": "userInput(logFileName, 'B')", 
                "Notes": "No Strategy"},

            1: {"Name": "Tic for Tat",
                "FunctionA": "titForTat_A(logFileName)", 
                "FunctionB": "titForTat_B(logFileName)", 
                "Notes": ""}, 

            2: {"Name": "Pavlov", 
                "FunctionA": "pavlov(logFileName, 'A')", 
                "FunctionB": "pavlov(logFileName, 'B')", 
                "Notes": ""}, 

            3: {"Name": "Adaptive Pavlov", 
                "FunctionA": "adaptivePavlov(logFileName, 'A')", 
                "FunctionB": "adaptivePavlov(logFileName, 'B')", 
                "Notes": ""}, 

            4: {"Name": "Suspicious Tit for Tat", 
                "FunctionA": "suspiciousTitForTat(logFileName, 'A')", 
                "FunctionB": "suspiciousTitForTat(logFileName, 'B')", 
                "Notes": ""}, 

            5: {"Name": "Tit for Two Tats", 
                "FunctionA": "titForTwoTats(logFileName, 'A')", 
                "FunctionB": "titForTwoTats(logFileName, 'B')", 
                "Notes": ""},

            6: {"Name": "Random", 
                "FunctionA": "random(logFileName, 'A')", 
                "FunctionB": "random(logFileName, 'B')", 
                "Notes": ""}, 

            7: {"Name": "All Cooperate", 
                "FunctionA": "allCooperate()", 
                "FunctionB": "allCooperate()", 
                "Notes": ""}, 

            8: {"Name": "All Defect", 
                "FunctionA": "allDefects(logFileName, 'A')", 
                "FunctionB": "allDefects(logFileName, 'B')", 
                "Notes": ""},

            9: {"Name": "Every Other", 
                "FunctionA": "everyOther(i)", 
                "FunctionB": "everyOther(i)", 
                "Notes": ""},

            10: {"Name": "GRIM", 
                "FunctionA": "grim(logFileName, 'A')", 
                "FunctionB": "grim(logFileName, 'B')", 
                "Notes": ""}, 

            11: {"Name": "Hill Climbing", 
                "FunctionA": "hillClimbing(logFileName)", 
                "Notes": ""},

            # 12: {"Name": "Genetic Algorithm V1 (No Memory)", 
            #     "FunctionA": "useGeneticV1('A', i, logFileName)", 
            #     "FunctionB": "useGeneticV1('B', i, logFileName)", 
            #     "Notes": ""},
            
            # 13: {"Name": "Genetic Algorithm V2 (1 Play Memory)", 
            #     "FunctionA": "useGeneticV2('A', i, logFileName)", 
            #     "FunctionB": "useGeneticV2('B', i, logFileName)", 
            #     "Notes": ""},
            
            # 14: {"Name": "Genetic Algorithm V3 (3 Plays Memory)", 
            #     "FunctionA": "useGeneticV3('A', i, logFileName)", 
            #     "FunctionB": "useGeneticV3('B', i, logFileName)", 
            #     "Notes": ""},
            12: {"Name": "Genetic Algorithm 1", "FunctionA": "getGeneticMove_A(i)", "FunctionB": "getGeneticMove_B(i)", "Notes": ""},
            # 13: {"Name": "Genetic Algorithm 2", "FunctionA": "getGenetic2Move_A(i, logFileName)", "FunctionB": "getGenetic2Move_B(i, logFileName)", "Notes": ""},
            14: {"Name": "Genetic Algorithm 2", "FunctionA": "getGenetic2Move_A(i, logFileName)", "FunctionB": "getGenetic2Move_B(i, logFileName)", "Notes": ""},
            15: {"Name": "Genetic Algorithm 3", "FunctionA": "getGenetic3Move_A(i, logFileName)", "FunctionB": "getGenetic3Move_B(i, logFileName)", "Notes": ""},
                       
         
        }

    def getCurrentScoreA(self) -> int:
        return self.scoreA
    
    def getCurrentScoreB(self) -> int:
        return self.scoreB


    # Set memorySize = -1 for entire round
    def simulate(self, strategyA, strategyB, logFileName= "Results/log.txt"):

        moveA = 0
        moveB = 0

        # Reset Score Before Starting:
        self.scoreA = 0
        self.scoreB = 0

        # with open(logFileName, "w") as file:
        file = open(logFileName, "w")
        # Clear the File
        file.close()
            # Loop through all the rounds
        for i in range(self.numOfRounds):
            # Find strategy for A:

            moveA = eval(self.menu[strategyA]["FunctionA"])
            
            # Find Strategy for B:

            moveB = eval(self.menu[strategyB]["FunctionB"])
            
            # Update log.txt:
            file = open(logFileName, "a")
            file.write(f"{moveA} {moveB}\n")
            file.close()

            # Update Total Score for Player A and B
            scores = self.playRound(moveA, moveB)
            self.scoreA += scores[0]
            self.scoreB += scores[1]


                
    

    # Returns pair of (scoreForPlayerA, scoreForPlayerB)
    def playRound(self, moveA, moveB) -> tuple[int,int]:
        if moveA == 0: 
            if moveB == 0:
                # Both Cooperate
                return (1, 1)
            else:
                # A Cooperates, B Deflects 
                return (20, 0)
            
        if moveA == 1:
            if moveB == 0:
                # A Deflects, B Cooperates
                return (0, 20)
            else:
                # Both Deflect
                return (10, 10)
        
        # If error occurs:
        return None


# Test Code for simulator

# testSim = Simulator(5)

# testSim.simulate(0,0)

# print(f"Score is {testSim.getCurrentScoreA()} vs {testSim.getCurrentScoreB()}")

# if __name__ == '__main__':

#     num_of_rounds = int(input("Enter a Number of Rounds: "))
#     a = int(input("Enter a ID of Strategy A: "))
#     b = int(input("Enter a ID of Strategy B: "))
#     sim = Simulator(numOfRounds= num_of_rounds)
#     sim.simulate(strategyA= a, strategyB= b)

#     print(f"Score is {sim.getCurrentScoreA()} vs {sim.getCurrentScoreB()}")



if __name__ == '__main__':
    sim = Simulator(numOfRounds= 10)

    # sim.simulate(4,0);
    # startGeneticv1(sim, 8)
    # startGeneticv2(sim, 8)
    # startGeneticv3(sim, 8)

    # startGeneticv1(sim, 16)
    # startGeneticv2(sim, 16)
    # startGeneticv3(sim, 16)

    # startGeneticv1(sim, 32)
    # startGeneticv2(sim, 32)
    # startGeneticv3(sim, 32)

    # startGeneticv1(sim, 64)
    # startGeneticv2(sim, 64)
    # startGeneticv3(sim, 64)

    # startGeneticv1(sim, 128)
    # startGeneticv2(sim, 128)
    # startGeneticv3(sim, 128)

    # startGeneticv3(sim, 64, 0)
    # startGeneticv3(sim, 64, 0.001)
    # startGeneticv3(sim, 64, 0.02)
    # startGeneticv3(sim, 64, 0.05)
    # startGeneticv3(sim, 64, 0.1)


    startGeneticv3(sim, 64, 0.5)
    startGeneticv3(sim, 64, 0.7)
    startGeneticv3(sim, 64, 0.8)
    startGeneticv3(sim, 64, 0.9)
    startGeneticv3(sim, 64, 0.95)
    startGeneticv3(sim, 64, 0.99)


