# Pavlov (or Win-stay, Lose-shift)
# Cooperates if it and its opponent moved alike in previous move and defects if they moved differently.

def pavlov(logFile, playerID):

    # Read existing log
    with open(logFile, 'r') as log:
        try:
            last_line = log.readlines()[-1]
        except IndexError:
            last_line = None

    # Close log for reading
    log.close()

    if (last_line is None):
        # Start with cooperate
        return 0
    else:
        # With at least one row of data Pavlov occurs
        if (last_line[0] == last_line[2]):
            return 0
        else:
            return 1
