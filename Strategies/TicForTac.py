import os

# from ..Simulator.main import Simulator

# OLD STUFF W/ FILES -> Does not work properly...
# def readLastNLines(n, fileName):
#     with open(fileName, "r") as file:
#         return file.readlines()[-n-1:-1]

# def titForTat(logFile, player):
#     if(not os.path.isfile(logFile) or os.stat(logFile).st_size == 0):
#         return 0
    
#     data = readLastNLines(1, logFile)
    
#     if player == 'A':
#         if(data[0][2] == '0'): 
#             return 1
#         return 0 
#     if player == 'B':
#         if(data[0][0] == '0'): 
#             return 1
#         return 0


def titForTat(lastMove):    
    print(lastMove)
    if(not lastMove): 
        return 0
    if(lastMove[0] == 0): 
        return 1
    else:
        return 0