import math

def tsp_bb(cities, start):
    n = len(cities)
    A = [1 << i for i in range(n)]

    # BEST DISTANCE IS SET TO BE INFINITY TO COMPARE GOTTEN DISTANCE
    best_dist = float('inf')
    best_path = []

    # THIS WHILE LOOP GOES THROUGH ALL POSSIBLE WAYS OF GOING THROUGH ALL THE CITIES EXAMPLE: 1, 3, 2, 0
    queue = [(start, 0, [], 0)]
    while queue:
        curr_node = queue.pop(0)
        curr_city, curr_dist, path, visited = curr_node
        path.append(curr_city)

        # THE IF CLAUSE WILL CHECK IF THE CITY HAS ALREADY BEEN VISITED
        if visited == (1 << n) - 1:
            total_dist = curr_dist + cities[curr_city][start]
            if total_dist < best_dist:
                best_dist = total_dist
                best_path = path.copy()
            continue

        # THIS FOR LOOP WILL ITERATE THROUGH THE CITIES AND CHECK IF ITS VISITED (pretty self explanatory)
        for next_city in range(n):
            if (1 << next_city) & visited:
                continue

            # COPY THE CURRENT PATH AND COMPARE IT TO THE NEW PATH
            new_path = path.copy()
            queue.append((next_city, curr_dist + cities[curr_city][next_city], new_path, visited | A[next_city]))
    best_path.append(start)
    return best_dist, best_path

# DISTANCE BETWEEN CITIES FROM EACH CITY.
cities = [[0,  49, 39, 40], [49,  0, 92,  46], [39,  92, 0,  22], [40, 46, 22,  0]]
start = 0

best_dist, best_path = tsp_bb(cities, start)
best_path.pop(0)
print("Best Distance:", best_dist)

print("Best Path:", best_path)