# Pavlov (or Win-stay, Lose-shift)
# Cooperates if it and its opponent moved alike in previous move and defects if they moved differently.

def pavlov(logFile, playerID):

    # Read existing log
    with open(logFile, 'r') as log:
        last_line = log.readlines()[-1]

    if (last_line is None):
        # Start with cooperate
        result = 0
    else:
        # With at least one row of data Pavlov occurs
        if (last_line[0] == last_line[2]):
            result = 0
        else:
            result = 1

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
