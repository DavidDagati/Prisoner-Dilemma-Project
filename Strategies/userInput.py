# User Input
# Will ask user for value 0 or 1

def userInput(logFile, playerID):

    # Set Result to Defect
    result = int(input(f"Player {playerID} Move: "))

    if (result in [0,1]):
        return result
    else:
        userInput(logFile, playerID)