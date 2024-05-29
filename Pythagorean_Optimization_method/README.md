# Traveling Salesman Brute Force (Pythagorean Theorem)
This document demonstrates a solution to the Traveling Salesman Problem (TSP) using brute-force permutation and calculation of distances with the Pythagorean theorem.

## Overview
The Traveling Salesman Problem (TSP) is a classic optimization problem where the objective is to find the shortest route that visits each location exactly once and returns to the starting location. This script employs brute-force permutation to generate all possible routes and calculates the total distance for each route using the Pythagorean theorem.

## Key Steps:
1. **Input Data**: Define the distances between locations and the deliveries to be made.
2. **Permutation Generation**: Generate all possible permutations of locations using itertools.permutations().
3. **Distance Calculation**: Calculate the total distance for each permutation using the distances matrix and the Pythagorean theorem.
4. **Optimal Route Selection**: Select the permutation with the minimum total distance as the optimal route.
5. **Output**: Print the optimal warehouse location and the total distance traveled.
  
---

## Example Output:
- Optimal warehouse location: pinomäki
- Total distance: 208.82111000000002

This script provides a simple yet effective approach to solving the Traveling Salesman Problem by exhaustively searching for the optimal route among all possible permutations of locations.
