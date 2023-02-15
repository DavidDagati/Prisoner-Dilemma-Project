import matplotlib.pyplot as plt
import json


file = open('../HillClimbing/Size10Iteration50Winners.json')
winners = json.load(file)
#print(winners)
file.close()

file = open('../HillClimbing/Size10Iteration50Wins.json')
wins = json.load(file)
#print(wins)
file.close()

for i in range(len(wins)):
    wins[i] = wins[i] * 2

print(winners)

colors = ['green', 'blue', 'purple', 'brown', 'teal', 'orange', 'red', 'peru', 'yellow', 'slateblue']
plt.barh(winners, wins, color=colors)
plt.title('Hill Climbing Optimization Results for Highest Score(Size: 10, Iterations: 50)', fontsize=14)
plt.xlabel('Wins (%)', fontsize=14)
plt.ylabel('Winners', fontsize=14)
plt.grid(True)

#hide y-axis
#ax = plt.gca()
#ax.get_yaxis().set_visible(False)

plt.show()