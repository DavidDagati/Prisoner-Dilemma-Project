
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
    def simulate(self, strategyA, strategyB, logFileName="Results/log.txt"):
        moveA = 0
        moveB = 0

        # Reset Score Before Starting:
        self.scoreA = 0
        self.scoreB = 0

        with open(logFileName, "w") as file:
            # Loop through all the rounds
            for i in range(self.numOfRounds):
                # Find strategy for A:
                if(strategyA == 0):
                    moveA = int(input("Player A Move: "))
                
                # Find Strategy for B:
                if(strategyB == 0):
                    moveB = int(input("Player B Move: "))
                
                # Update Total Score for Player A and B
                scores = self.playRound(moveA, moveB)
                self.scoreA += scores[0]
                self.scoreB += scores[1]
                # Update log.txt:
                file.write(f"{moveA} {moveB}\n")

                
    

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


