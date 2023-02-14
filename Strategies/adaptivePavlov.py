import os  

def tit_for_tat(last_line, opponentSpace):
    if (last_line[opponentSpace] == "0"):
        return 0    
    return 1

def allDefect():    
    return 1


def adaptivePavlov(logFile, playerID):
    # Opens log file
    with open(logFile, "r") as file:
        try:
            lines = file.read().splitlines()
            count = len(lines)
            last_line = lines[-1]
        except IndexError:
            last_line = None
        
        # if (count >= 6):
        #     for i in range (0,6):
        #         try:
        #             lines[i] = file.readlines()[i]
        #         except:
        #             pass
                
    # Defining the opponent position
    opponentSpace = 2 if playerID == 0 else 0
    
    # For first 6 moves, the technique follows tit for tat
    if (count < 6):
        # Tit For Tat
        if count == 0:
            return 0
        return tit_for_tat(last_line, opponentSpace)
    else:
    # For the rest of the moves it will adapt to the corresponding strategies
        strategyTypes = {
            0: "allCooperate",
            1: "allDefects",
            2: "random",
            3: "titForTat",
            4: "pavlov",
        }

        #The best strategy to go 0,3,4 is tit for tat
        if (lines[0][opponentSpace] == "1" and lines[1][opponentSpace] == "1" and lines[2][opponentSpace] == "1" and lines[3][opponentSpace] == "1" and lines[4][opponentSpace] == "1" and lines[5][opponentSpace] == "1"):
            return tit_for_tat(last_line, playerID)
        #The best strategy to go 1, 2 is always defect
        else:
            return allDefect()
        

# Test:
#print(adaptivePavlov('../Results/log.txt', 1))