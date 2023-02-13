# GRIM
# Cooperates unless defected against once, then defects always

def grim(logFile, playerID):

    # Read existing log
    with open(logFile, 'r') as log:
        try:
            lines = log.read().splitlines()
            last_line = lines[-1]
        except IndexError:
            last_line = None
            
    # Close log for reading
    log.close()

    if (last_line == None):
        return 0

    # Select position based on PlayerID
    if (playerID == "A"):
        position = 2
    elif (playerID == "B"):
        position = 0

    coop_count = 0

    for row in lines:
        if int(row[position]) == 1:
            return 1
        elif int(row[position]) == 0:
            coop_count += 1
    
    if coop_count == len(lines):
        return 0