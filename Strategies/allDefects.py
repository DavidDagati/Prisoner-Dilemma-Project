# All Defect
# Will always Defect no matter what

def allDefects(logFile, playerID):

    # Set Result to Defect
    result = 1

    # Open the logFile for appending
    log = open(logFile, 'a')

    # Write the result in logFile
    if playerID == "A":
        log.write("\n" + result)
    elif playerID == "B":
        log.write(" " + result)

    # Close log for appending
    log.close()