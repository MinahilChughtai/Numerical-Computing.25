import numpy as np

# Population data
years = list(range(2015, 2026))
population = [10000, 10500, 11000, 11700, 12500, 13000, 13800, 14500, 15300, 16000, 16800]

# a) Year-to-year increase (AP)
AP = [population[i] - population[i-1] for i in range(1, len(population))]

# b) Change in population (VP) compared to previous year
VP = [AP[i] - AP[i-1] for i in range(1, len(AP))]

# c) Average change in population between two years
average_change = [(AP[i] + AP[i-1]) / 2 for i in range(1, len(AP))]

# d) Mean population over the decade
mean_population = sum(population) / len(population)

# e) Predict population for 2026 using the shifting operator
predicted_population_2026 = population[-1] + AP[-1]

# Display results
print("Year-to-Year Increase (AP):", AP)
print("Change in Population (VP):", VP)
print("Average Change in Population:", average_change)
print("Mean Population over the decade:", mean_population)
print("Predicted Population for 2026:", predicted_population_2026)
