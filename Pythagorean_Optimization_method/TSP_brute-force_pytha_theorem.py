from itertools import permutations

# CALCULATONS ARE CALCULATES WITH PYTHAGOREAN THEOREM
distances = [[0, 2.23607, 7.61577, 11.4018, 7.07107, 8.544],
             [2.23607, 0, 6.40312, 9.43398, 7.61577, 7.07107],
             [7.61577, 6.40312, 0, 12, 14.1421, 12.6491],
             [11.4018, 9.43398, 12, 0, 9.21954, 4.12311],
             [7.07107, 7.61577, 14.1421, 9.21954, 0, 4.12311],
             [8.544, 7.07107, 12.6491, 4.12311, 4.12311, 0]]

deliveries = [90, 130, 105, 60, 120]
indices = list(range(len(deliveries)))
perms = permutations(indices)
min_distance = float('inf')
optimal_perm = None


for perm in perms:
    distance = 0
    prev_location = 0  # WAREHOUSE LOCATION
    for index in perm:
        location = index + 1 
        distance += distances[prev_location][location]
        prev_location = location

    distance += distances[prev_location][0]

    # IF DISTANCE = SMALLER THAN PREVIOUS MIN DISTANCE, CHANGE PARAMS
    if distance < min_distance:
        min_distance = distance
        optimal_perm = perm

locations = ['warehouse', 'pinomäki', 'vähärauma', 'harjunpää', 'friitala', 'vihelä']
optimal_locations = [locations[i+1] for i in optimal_perm]
print("Optimal warehouse location:", optimal_locations[0])
print("Total distance:", min_distance)
