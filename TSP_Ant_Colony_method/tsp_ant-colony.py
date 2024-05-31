import math
import random

class ACOParameters:
    def __init__(self, num_ants, evaporation_rate, alpha, beta, q0):
        self.num_ants = num_ants  # how many ants
        self.evaporation_rate = evaporation_rate  # pheromone evaporation rate
        self.alpha = alpha  # pheromone trail
        self.beta = beta  # heuristic information
        self.q0 = q0  # probability of exploiting the best known solution

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initialize_pheromone_matrix(num_cities, initial_pheromone):
    return [[initial_pheromone] * num_cities for _ in range(num_cities)]

def initialize_heuristic_matrix(cities):
    num_cities = len(cities)
    heuristic_matrix = [[0.0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                heuristic_matrix[i][j] = 1.0 / calculate_distance(cities[i], cities[j])
    return heuristic_matrix

def ant_colony_optimization(cities, start, parameters):
    num_cities = len(cities)
    pheromone_matrix = initialize_pheromone_matrix(num_cities, 1.0)
    heuristic_matrix = initialize_heuristic_matrix(cities)

    best_path = None
    best_distance = float('inf')

    for _ in range(parameters.num_ants):
        ant = start
        visited_cities = [ant]
        remaining_cities = list(range(num_cities))
        remaining_cities.remove(ant)

        while remaining_cities:
            probabilities = []
            for city in remaining_cities:
                pheromone = pheromone_matrix[ant][city] ** parameters.alpha
                heuristic = heuristic_matrix[ant][city] ** parameters.beta
                probabilities.append(pheromone * heuristic)
            
            if random.random() < parameters.q0:
                max_prob = max(probabilities)
                next_city = remaining_cities[probabilities.index(max_prob)]
            else:
                total_prob = sum(probabilities)
                probabilities = [p / total_prob for p in probabilities]
                next_city = random.choices(remaining_cities, probabilities)[0]

            # update ants position and visited cities
            ant = next_city
            visited_cities.append(ant)
            remaining_cities.remove(ant)
            
        distance = sum(calculate_distance(cities[i], cities[j]) for i, j in zip(visited_cities, visited_cities[1:] + visited_cities[:1]))

        # update the best path and distance if a wayy is found
        if distance < best_distance:
            best_distance = distance
            best_path = visited_cities

        for i, j in zip(visited_cities, visited_cities[1:] + visited_cities[:1]):
            pheromone_matrix[i][j] += 1.0 / distance

    return best_distance, best_path

cities = [[0, 49, 39, 40], [49, 0, 92, 46], [39, 92, 0, 22], [40, 46, 22, 0]]
start = 0

# parameters
num_ants = 10
evaporation_rate = 0.5
alpha = 1.0
beta = 2.0
q0 = 0.9
parameters = ACOParameters(num_ants, evaporation_rate, alpha, beta, q0)

best_distance, best_path = ant_colony_optimization(cities, start, parameters)
print("Best Distance:", best_distance) # output: 220.23
print("Best Path:", best_path) # output: 0, 2, 3, 1

# Calculate_distance calculate the euclidean distance between cities
# initialize_pheromone_matrix is used to initialize the pheromone matrix and same with initialize_heuristic_matrix

# the func ant_colony_optimization uses the aco aglorithm. It constructs solutions using ants defined in the parameters.
# then it uses the pheromone and heuristic information for deciding which city is next.