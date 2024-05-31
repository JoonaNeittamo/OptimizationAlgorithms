import random
import math

def distance(city1, city2): #euclidian
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tsp_genetic(cities, start, population_size, generations):
    n = len(cities)
    A = [1 << i for i in range(n)]

    population = []
    for _ in range(population_size):
        tour = list(range(n))
        random.shuffle(tour)
        population.append(tour)

    def calculate_fitness(tour):
        dist = 0
        for i in range(n - 1):
            dist += distance(cities[tour[i]], cities[tour[i+1]])
        dist += distance(cities[tour[-1]], cities[tour[0]])
        return dist

    for _ in range(generations):
        fitness_scores = [calculate_fitness(tour) for tour in population]

        selected_parents = []
        for _ in range(population_size):
            tournament_size = 5
            tournament = random.sample(range(population_size), tournament_size)
            selected_parent = min(tournament, key=lambda x: fitness_scores[x])
            selected_parents.append(population[selected_parent])

        children = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected_parents[i], selected_parents[i+1]
            start_index = random.randint(0, n - 1)
            end_index = random.randint(start_index + 1, n)
            child1 = parent1[start_index:end_index] + [city for city in parent2 if city not in parent1[start_index:end_index]]
            child2 = parent2[start_index:end_index] + [city for city in parent1 if city not in parent2[start_index:end_index]]
            children.extend([child1, child2])

        for child in children: # alteration of children
            if random.random() < 0.1:
                index1, index2 = random.sample(range(n), 2)
                child[index1], child[index2] = child[index2], child[index1]

        population = children

    best_tour = min(population, key=lambda tour: calculate_fitness(tour))
    best_dist = calculate_fitness(best_tour)
    best_path = [start] + best_tour + [start]

    return best_dist, best_path

# Change params to get better (or worse, depends) results
cities = [[0, 49, 39, 40], [49, 0, 92, 46], [39, 92, 0, 22], [40, 46, 22, 0]] # cities
start = 0
population_size = 50
generations = 1000

best_dist, best_path = tsp_genetic(cities, start, population_size, generations)
print("Best Distance:", best_dist)
print("Best Path:", best_path)


# distance function is used to calculate the euclidean distance in current two cities selected. 
# tsp_genetic uses GA on it which will then create population, fitness and does the choosing. Also alteration is performed.
# at the end the tsp_genetic will create generations and "discard" worse selections.

# best_dist outcome: 220.23
# best_path outcome: 0, 0, 2, 3, 1, 0