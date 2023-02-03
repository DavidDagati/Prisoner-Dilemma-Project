# Tit For Two Tats: TFTT (or TF2T)
# Cooperates unless defected against twice in a row.

def titForTwoTats(logFile, playerID):

    # Read existing log
    with open(logFile, 'r') as log:
        try:
            lines = log.read().splitlines()
            last_line = lines[-1]
        except IndexError:
            last_line = None

        try:
            second_last_line = lines[-2]
        except IndexError:
            second_last_line = None
            

    # Close log for reading
    log.close()

    if ((last_line is None) or (second_last_line is None)):
        # Start with cooperate
        return 0
    else:
        # Select position based on PlayerID
        if (playerID == "A"):
            position = 2
        elif (playerID == "B"):
            position = 0
        # With at least two rows of data TFTT occurs
        if ((int(last_line[position]) == 1) and (int(second_last_line[position]) == 1)):
            return 1
        else:
            return 0
