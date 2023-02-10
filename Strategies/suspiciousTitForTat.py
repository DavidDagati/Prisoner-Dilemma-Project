import os  

def suspiciousTitForTat(logFile, playerID):
    with open(logFile, "r") as file:
        last_line = file.readlines()[-1]
    
    if os.path.getsize(logFile) == 0:
        return 0
    
    opponentSpace = 2 if playerID == 0 else 0
        
    if (last_line[opponentSpace] == "0"):
        return 0    
    return 1

# Test:
# print(suspiciousTitForTat('../Results/log.txt', 1))
