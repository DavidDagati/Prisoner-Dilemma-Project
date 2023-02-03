import os

def readLastLine(fileName):
    if(not os.path.isfile(fileName) or os.stat(fileName).st_size == 0): return None

    with open(fileName, "r") as file:
        return file.readlines()[-1]

def titForTat_A(logFile):
    test = readLastLine(logFile)
    if(not test): return 0

    if(test[2] == "0"): return 1

    return 0

def titForTat_B(logFile):
    test = readLastLine(logFile)
    if(not test): return 0

    if(test[0] == "0"): return 1

    return 0
