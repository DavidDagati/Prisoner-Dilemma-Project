
import os
import json

def readLast_n_Lines(n, fileName):
    if(not os.path.isfile(fileName) or os.stat(fileName).st_size == 0): return None

    with open(fileName, "r") as file:
        return file.readlines()[-n:]

def useGeneticV3(ltr, round, logFile):
    if(round >= 10):
        round = ((round-3) % 7) + 3 

    with open('Results/GeneticPlays_Final/genetic3_pop64.json', 'r') as file_object:  
        data = json.load(file_object)  
        if(ltr == 'A'):
            return getGenetic3Move_A(round, logFile, data, 2)
        else:
            return getGenetic3Move_A(round, logFile, data, 0)

def useGeneticV2(ltr, round, logFile):
    if(round >= 10):
        round = ((round-1) % 9) + 1     
    with open('Results/GeneticPlays/genetic2_pop32.json', 'r') as file_object:  
        data = json.load(file_object)  
        if(ltr == 'A'):
            return getGenetic2Move_A(round, logFile, data, 2)
        else:
            return getGenetic2Move_A(round, logFile, data, 0)

def useGeneticV1(ltr, round, logFile):
    if(round >= 6):
        round = round % 6 
    with open('Results/GeneticPlays/genetic1_pop32.json', 'r') as file_object:  
        data = json.load(file_object) 
        if(ltr == 'A'): 
            return getGenetic1Move_A(round, data)
        else:
            return getGenetic1Move_A(round, data)

def getGenetic1Move_A(round, movesA):
    return movesA[round]


def getGenetic2Move_A(round, logFile, movesA, read_col):
    if(round == 0): return movesA[0]

    test = (readLast_n_Lines(1, logFile))[0]

    if(test[read_col] == "0"): movesA[round][0]

    return movesA[round][1]


def getGenetic3Move_A(round, logFile, movesA, read_col):
    if(round == 0): return movesA[0]

    if(round == 1):
        test = readLast_n_Lines(1, logFile)
        if(test[0][read_col] == "0"): return movesA[round][0]
        return movesA[round][1]
    
    if(round == 2):
        test = readLast_n_Lines(2, logFile)
        if(test[1][read_col] == "0"):
            if(test[0][read_col] == "0"):
                return movesA[round][0] 
            return movesA[round][1] 
        else:
            if(test[0][read_col] == "0"):
                return movesA[round][2] 
            return movesA[round][3] 

    else:
        test = readLast_n_Lines(3, logFile)
        if(test[2][read_col] == "0"):
            if(test[1][read_col] == "0"):
                if(test[0][read_col] == "0"):
                    return movesA[round][0] 
                return movesA[round][1] 
            else:
                if(test[0][read_col] == "0"):
                    return movesA[round][2] 
                return movesA[round][3] 
        else:
            if(test[1][read_col] == "0"):
                if(test[0][read_col] == "0"):
                    return movesA[round][4] 
                return movesA[round][5] 
            else:
                if(test[0][read_col] == "0"):
                    return movesA[round][6] 
                return movesA[round][7] 
