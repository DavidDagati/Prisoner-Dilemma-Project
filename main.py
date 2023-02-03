
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
# from Strategies.ticForTat import ticForTat
from Strategies.pavlov import pavlov
# from Strategies.adaptivePavlov import adaptivePavlov
# from Strategies.suspiciousTitForTat import suspiciousTitForTat
from Strategies.titForTwoTats import titForTwoTats
# from Strategies.random import random
# from Strategies.allCooperate import allCooperate
from Strategies.allDefects import allDefects
# from Strategies.everyOther import everyOther
# from Strategies.grim import grim
# from Strategies.everyOther import everyOther
# from Optimizations.hillClimbing import hillClimbing
# from Optimizations.geneticAlgorithm import geneticAlgorithm


class Simulator:
    def __init__(self, numOfRounds):
        self.numOfRounds = numOfRounds
        self.scoreA = 0
        self.scoreB = 0

    def getCurrentScoreA(self) -> int:
        return self.scoreA
    
    def getCurrentScoreB(self) -> int:
        return self.scoreB


    # Set memorySize = -1 for entire round
    def simulate(self, strategyA, strategyB, logFileName= "Results/log.txt"):

        menu = {
            0: {"Name": "UserInput", "FunctionA": "userInput(logFileName, 'A')", "FunctionB": "userInput(logFileName, 'B')", "Notes": "No Strategy"},
            1: {"Name": "Tic for Tat", "FunctionA": "ticForTat(logFileName, 'A')", "FunctionB": "ticForTat(logFileName, 'B')", "Notes": ""}, 
            2: {"Name": "Pavlov", "FunctionA": "pavlov(logFileName, 'A')", "FunctionB": "pavlov(logFileName, 'B')", "Notes": ""}, 
            3: {"Name": "Adaptive Pavlov", "FunctionA": "adaptivePavlov(logFileName, 'A')", "FunctionB": "adaptivePavlov(logFileName, 'B')", "Notes": ""}, 
            4: {"Name": "Suspicious Tit for Tat", "FunctionA": "suspiciousTitForTat(logFileName, 'A')", "FunctionB": "suspiciousTitForTat(logFileName, 'B')", "Notes": ""}, 
            5: {"Name": "Tit for Two Tats", "FunctionA": "titForTwoTats(logFileName, 'A')", "FunctionB": "titForTwoTats(logFileName, 'B')", "Notes": ""},
            6: {"Name": "Random", "FunctionA": "random(logFileName, 'A')", "FunctionB": "random(logFileName, 'B')", "Notes": ""}, 
            7: {"Name": "All Cooperate", "FunctionA": "allCooperate(logFileName, 'A')", "FunctionB": "allCooperate(logFileName, 'B')", "Notes": ""}, 
            8: {"Name": "All Defect ", "FunctionA": "allDefects(logFileName, 'A')", "FunctionB": "allDefects(logFileName, 'B')", "Notes": ""},
            9: {"Name": "Every Other ", "FunctionA": "everyOther(logFileName, 'A')", "FunctionB": "everyOther(logFileName, 'B')", "Notes": ""},
            10: {"Name": "GRIM", "FunctionA": "grim(logFileName, 'A')", "FunctionB": "grim(logFileName, 'B')", "Notes": ""}, 
            11: {"Name": "Hill Climbing", "FunctionA": "hillClimbing(logFileName)", "Notes": ""},
            12: {"Name": "Genetic Algorithm", "FunctionA": "geneticAlgorithm(logFileName)", "Notes": ""},
            # 13: {"Name": "", "FunctionA": "", "Notes": ""},
        }
        
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

            moveA = eval(menu[strategyA]["FunctionA"])
            
            # Find Strategy for B:

            moveB = eval(menu[strategyB]["FunctionB"])
            
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

if __name__ == '__main__':

    num_of_rounds = int(input("Enter a Number of Rounds: "))
    a = int(input("Enter a ID of Strategy A: "))
    b = int(input("Enter a ID of Strategy B: "))
    sim = Simulator(numOfRounds= num_of_rounds)
    sim.simulate(strategyA= a, strategyB= b)

