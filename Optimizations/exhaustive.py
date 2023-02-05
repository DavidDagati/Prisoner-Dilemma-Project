# The Exhaustive search method (Brute Force)

from datetime import datetime

from main import Simulator

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
        