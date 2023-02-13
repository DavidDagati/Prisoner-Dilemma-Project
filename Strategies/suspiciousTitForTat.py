import os  

# Fixed Suspicious Tit-For-Tat:
# Moved if os.path... to the top of the function

def suspiciousTitForTat(logFile, playerID):
    if os.path.getsize(logFile) == 0:
        return 1
    with open(logFile, "r") as file:
        last_line = file.readlines()[-1]
    
    opponentSpace = 2 if playerID == 0 else 0
        
    if (last_line[opponentSpace] == "0"):
        return 0    
    return 1

# Test:
# print(suspiciousTitForTat('../Results/log.txt', 1))
