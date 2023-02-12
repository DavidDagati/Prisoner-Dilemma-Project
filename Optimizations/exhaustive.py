# The Exhaustive search method (Brute Force)

import sys
import os
import json
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

def exhaustive():

    session_name = input("Enter a Session Name: ")
    num_of_rounds = int(input("Enter a Number of Rounds: "))

    session = {
                    "Session Name": session_name,
                    "Number of Rounds": num_of_rounds,
                    "Session Data": {}
            }

    # strategies = ["adaptivePavlov", "allCooperate", "allDefects", "everyOther", "grim", "pavlov", "random", "suspiciousTitForTat", "ticForTac", "titForTwoTats"]

    cycle_count = 0

    for i in range(1,11): # strategy_A in strategies:

        for j in range(1,11): # strategy_B in strategies:

            cycle_count += 1

            start = datetime.now().strftime("%H:%M:%S")
            try:
                sim = Simulator(numOfRounds= num_of_rounds)
                sim.simulate(strategyA= i, strategyB= j)
            except:
                print(f"Missing {sim.menu[i]['Name']} or {sim.menu[j]['Name']}")
            end = datetime.now().strftime("%H:%M:%S")

            if sim.getCurrentScoreA() > sim.getCurrentScoreB():
                winner = sim.menu[i]['Name']
            elif sim.getCurrentScoreA() < sim.getCurrentScoreB():
                winner = sim.menu[j]['Name']
            else:
                winner = "Tie"

            # Update Score results log:
            round_data = {
                            "Strategy A": sim.menu[i]['Name'],
                            "Strategy B": sim.menu[j]['Name'],
                            "Start Time": start,
                            "End Time": end,
                            "Strategy A Score": sim.getCurrentScoreA(),
                            "Strategy B Score": sim.getCurrentScoreB(),
                            "Winner": winner
                        }
            session["Session Data"][cycle_count] = round_data
            
    with open('Results\exhaustive_log.json', 'a') as file:
        json.dump(session, file)



def rankScore():
    # read log winners and rank based on score and how often
    # one for score one for time
    # append #-of-rounds to filename
    # run 5 times 
    # graph y axis rounds
    # x axis strategies 

    with open('Results\exhaustive_log.json', 'r') as file:
        e_log = json.load(file)

        y = ["Adaptive Pavlov", "All Cooperate", "All Defects", "Every Other", "Grim", "Pavlov", "Random", "Suspicious Tit For Tat", "Tic For Tac", "Tit For Two Tats", "Tie"]

        ap_count = 0
        ac_count = 0
        ad_count = 0
        eo_count = 0
        g_count = 0
        p_count = 0
        r_count = 0
        st4t_count = 0
        t4t_count = 0
        t4tt_count = 0
        tie_count = 0

        for cycle in e_log["Session Data"]:
            if e_log["Session Data"][cycle]["Winner"] == "Tic for Tat":
                t4t_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Pavlov":
                p_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Adaptive Pavlov":
                ap_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Suspicious Tit for Tat":
                st4t_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Tit for Two Tats":
                t4tt_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Random":
                r_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "All Cooperate":
                ac_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "All Defect":
                ad_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Every Other":
                eo_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "GRIM":
                g_count += 1
            elif e_log["Session Data"][cycle]["Winner"] == "Tie":
                tie_count += 1

        x = [ap_count, ac_count, ad_count, eo_count, g_count, p_count, r_count, st4t_count, t4t_count, t4tt_count, tie_count]

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        y_pos = np.arange(len(y))
        error = np.random.rand(len(y))

        ax.barh(y_pos, x, xerr=error, align='center')
        ax.set_yticks(y_pos, labels=y)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Score')
        ax.set_title('Exhaustive Winner Count')

        plt.show()
                
    return

def rankTime():
    # read log winners and rank based on score and how often
    # one for score one for time
    # append #-of-rounds to filename
    # run 5 times 
    # graph y axis rounds
    # x axis strategies 
    return
        
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
    rankScore()