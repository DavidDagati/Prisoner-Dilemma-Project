# Tit For Two Tats: TFTT (or TF2T)
# Cooperates unless defected against twice in a row.

def titForTwoTats(logFile, playerID):

    # Read existing log
    with open(logFile, 'r') as log:
        second_last_line = log.readlines()[-2]
        last_line = log.readlines()[-1]

    if ((last_line is None) or (second_last_line is None)):
        # Start with cooperate
        result = 0
    else:
        # Select position based on PlayerID
        if (playerID == "A"):
            position = 2
        elif (playerID == "B"):
            position = 0
        # With at least two rows of data TFTT occurs
        if ((last_line[position] == 1) and (second_last_line[position] == 1)):
            result = 1
        else:
            result = 0

    # Close log for reading
    log.close()

    # Open the logFile for appending
    log = open(logFile, 'a')

    # Write the result in logFile
    if playerID == "A":
        log.write("\n" + result)
    elif playerID == "B":
        log.write(" " + result)

    # Close log for appending
    log.close()