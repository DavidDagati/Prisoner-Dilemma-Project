import matplotlib.pyplot as plt
import numpy as np
import json



'''
AVERAGES FOR EACH VERSION
'''

# with open('GeneticData_PopulationTest/genetic3_scores_averages_8.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.ylim([20, 80])
#     plt.plot(ypoints, color = 'blue')



# with open('GeneticData_PopulationTest/genetic3_scores_averages_16.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'red')



# with open('GeneticData_PopulationTest/genetic3_scores_averages_32.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'orange')


# with open('GeneticData_PopulationTest/genetic3_scores_averages_64.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)


#     plt.plot(ypoints, color = 'green')



# with open('GeneticData_PopulationTest/genetic3_scores_averages_128.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)
#     plt.ylim([20, 80])

#     plt.plot(ypoints, color = 'purple')
#     plt.xlabel('Generation Number') 
#     plt.ylabel('Score') 
#     plt.title("Genetic V3 Average Scores (Various Population Sizes)")
#     plt.legend(['Population = 8', 'Population = 16', 'Population = 32', 'Population = 64', 'Population = 128'], loc='upper left')

#     plt.savefig('GeneticDiagrams/genetic3_pop_comparison.png')
#     plt.show()


# with open('GeneticData_PopulationTest/genetic2_scores_averages_8.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.ylim([20, 80])
#     plt.plot(ypoints, color = 'blue')



# with open('GeneticData_PopulationTest/genetic2_scores_averages_16.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'red')



# with open('GeneticData_PopulationTest/genetic2_scores_averages_32.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'orange')


# with open('GeneticData_PopulationTest/genetic2_scores_averages_64.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)


#     plt.plot(ypoints, color = 'green')



# with open('GeneticData_PopulationTest/genetic2_scores_averages_128.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)
#     plt.ylim([20, 80])

#     plt.plot(ypoints, color = 'purple')
#     plt.xlabel('Generation Number') 
#     plt.ylabel('Score') 
#     plt.title("Genetic V2 Average Scores (Various Population Sizes)")
#     plt.legend(['Population = 8', 'Population = 16', 'Population = 32', 'Population = 64', 'Population = 128'], loc='upper left')

#     plt.savefig('GeneticDiagrams/genetic2_pop_comparison.png')
#     plt.show()

# with open('GeneticData_PopulationTest/genetic1_scores_averages_8.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.ylim([20, 80])
#     plt.plot(ypoints, color = 'blue')



# with open('GeneticData_PopulationTest/genetic1_scores_averages_16.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'red')



# with open('GeneticData_PopulationTest/genetic1_scores_averages_32.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'orange')


# with open('GeneticData_PopulationTest/genetic1_scores_averages_64.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)


#     plt.plot(ypoints, color = 'green')



# with open('GeneticData_PopulationTest/genetic1_scores_averages_128.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)
#     plt.ylim([20, 80])

#     plt.plot(ypoints, color = 'purple')
#     plt.xlabel('Generation Number') 
#     plt.ylabel('Score') 
#     plt.title("Genetic V1 Average Scores (Various Population Sizes)")
#     plt.legend(['Population = 8', 'Population = 16', 'Population = 32', 'Population = 64', 'Population = 128'], loc='upper left')

#     plt.savefig('GeneticDiagrams/genetic1_pop_comparison.png')
#     plt.show()


'''
COMPARISON FOR EACH VERSION
'''

# with open('GeneticData_PopulationTest/genetic1_scores_averages_32.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'orange')


# with open('GeneticData_PopulationTest/genetic2_scores_averages_32.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)


#     plt.plot(ypoints, color = 'green')



# with open('GeneticData_PopulationTest/genetic3_scores_averages_128.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)
#     plt.ylim([20, 60])

#     plt.plot(ypoints, color = 'purple')
#     plt.xlabel('Generation Number') 
#     plt.ylabel('Fitness') 
#     plt.title("Genetic Versions Compared")
#     plt.legend(['Genetic V1 (Pop 32)', 'Genetic V2 (Pop 32)', 'Genetic V3 (Pop 128)',], loc='upper left')

#     plt.savefig('GeneticDiagrams/genetic_memory_comparision.png')
#     plt.show()


'''
Crossover Test FOR VERSION 3
'''

with open('GeneticData_Crossover/genetic3_scores_averages_0.5.json', 'r') as file_object:  
    data = json.load(file_object)  
    ypoints = np.array(data)

    plt.ylim([20, 60])
    plt.plot(ypoints, color = 'blue')



with open('GeneticData_Crossover/genetic3_scores_averages_0.7.json', 'r') as file_object:  
    data = json.load(file_object)  
    ypoints = np.array(data)

    plt.plot(ypoints, color = 'red')



with open('GeneticData_Crossover/genetic3_scores_averages_0.8.json', 'r') as file_object:  
    data = json.load(file_object)  
    ypoints = np.array(data)

    plt.plot(ypoints, color = 'orange')


with open('GeneticData_Crossover/genetic3_scores_averages_0.9.json', 'r') as file_object:  
    data = json.load(file_object)  
    ypoints = np.array(data)


    plt.plot(ypoints, color = 'green')

with open('GeneticData_Crossover/genetic3_scores_averages_0.95.json', 'r') as file_object:  
    data = json.load(file_object)  
    ypoints = np.array(data)


    plt.plot(ypoints, color = 'yellow')



with open('GeneticData_Crossover/genetic3_scores_averages_0.99.json', 'r') as file_object:  
    data = json.load(file_object)  
    ypoints = np.array(data)
    plt.ylim([20, 80])

    plt.plot(ypoints, color = 'purple')
    plt.xlabel('Generation Number') 
    plt.ylabel('Score') 
    plt.title("Genetic V3 Average Scores (Population of 128, Mutation Probility of 0.001)")
    plt.legend(['Crossover Probability = 0.5', 'Crossover Probability = 0.7', 'Crossover Probability = 0.8', 'Crossover Probability = 0.9', 'Crossover Probability = 0.95', 'Crossover Probability = 0.99'], loc='upper left')

    plt.savefig('GeneticDiagrams/genetic3_avg_all_crossover_norandom.png')
    plt.show()


'''
 Mutation Test FOR VERSION 3
'''

# with open('GeneticData_Mutations/genetic3_scores_averages_0.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     # plt.ylim([20, 60])
#     plt.plot(ypoints, color = 'blue')



# with open('GeneticData_Mutations/genetic3_scores_averages_0.001.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'red')



# with open('GeneticData_Mutations/genetic3_scores_averages_0.02.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'orange')


# with open('GeneticData_Mutations/genetic3_scores_averages_0.05.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)


#     plt.plot(ypoints, color = 'green')



# with open('GeneticData_Mutations/genetic3_scores_averages_0.1.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)
#     plt.ylim([20, 80])

#     plt.xlim([0,100])

#     plt.plot(ypoints, color = 'purple')
#     plt.xlabel('Generation Number') 
#     plt.ylabel('Score') 
#     plt.title("Genetic V3 Average Scores for Mutations")
#     plt.legend(['Mutation Probability = 0.000', 'Mutation Probability = 0.001', 'Mutation Probability = 0.020', 'Mutation Probability = 0.050', 'Mutation Probability = 0.100'], loc='upper left')

#     plt.savefig('GeneticDiagrams/genetic3_mutations_rand.png')
#     plt.show()


'''
Mutation Test FOR VERSION 3 -> NO RANDOM
'''

# with open('GeneticData_Mutations_NoRAND/genetic3_scores_averages_0.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     # plt.ylim([20, 60])
#     plt.plot(ypoints, color = 'blue')



# with open('GeneticData_Mutations_NoRAND/genetic3_scores_averages_0.001.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'red')



# with open('GeneticData_Mutations_NoRAND/genetic3_scores_averages_0.02.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)

#     plt.plot(ypoints, color = 'orange')


# with open('GeneticData_Mutations_NoRAND/genetic3_scores_averages_0.05.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)


#     plt.plot(ypoints, color = 'green')



# with open('GeneticData_Mutations_NoRAND/genetic3_scores_averages_0.1.json', 'r') as file_object:  
#     data = json.load(file_object)  
#     ypoints = np.array(data)
#     plt.ylim([20, 80])

#     plt.xlim([0,100])

#     plt.plot(ypoints, color = 'purple')
#     plt.xlabel('Generation Number') 
#     plt.ylabel('Score') 
#     plt.title("Genetic V3 Average Scores for Mutations")
#     plt.legend(['Mutation Probability = 0.000', 'Mutation Probability = 0.001', 'Mutation Probability = 0.020', 'Mutation Probability = 0.050', 'Mutation Probability = 0.100'], loc='upper left')

#     plt.savefig('GeneticDiagrams/genetic3_mutations_NO_rand.png')
#     plt.show()


