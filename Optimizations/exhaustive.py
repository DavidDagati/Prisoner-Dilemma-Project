# The Exhaustive search method (Brute Force)

import sys
import os

from datetime import datetime

def exhaustive():

    num_of_rounds = int(input("Enter a Number of Rounds: "))

    # strategies = ["adaptivePavlov", "allCooperate", "allDefects", "everyOther", "grim", "pavlov", "random", "suspiciousTitForTat", "ticForTac", "titForTwoTats"]

    cycle_count = 0

    for i in range(1,11): # strategy_A in strategies:

        for j in range(1,11): # strategy_B in strategies:

            cycle_count += 1

            start = datetime.now().strftime("%H:%M:%S")

            sim = Simulator(numOfRounds= num_of_rounds)
            sim.simulate(strategyA= i, strategyB= j)

            end = datetime.now().strftime("%H:%M:%S")

        # Update Score results log:
        file = open("Results\exhaustive_log.txt", "a")
        file.write(f"Cycle {cycle_count} ({start} to {end}) with {num_of_rounds} Rounds: {sim.menu[i]['Name']}: {sim.scoreA} {sim.menu[j]['Name']}: {sim.scoreB} Winner: {max(sim.scoreA, sim.scoreB)}\n")
        file.close()
        

if __name__ == "__main__":
    # Get current Directory
    current = os.path.dirname(os.path.realpath(__file__))
    
    # Get Parent Directory
    parent = os.path.dirname(current)
    
    # Adding parent directory to sys.path.
    sys.path.append(parent)
    
    # Now able to import Simulator
    from main import Simulator

    exhaustive()