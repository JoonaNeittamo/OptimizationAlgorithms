# Traveling Salesman Problem Ant Colony Optimization

This document demonstrates a solution to the Traveling Salesman Problem (TSP) using an Ant Colony Optimization (ACO) algorithm. The goal is to find the shortest route that visits each city exactly once and returns to the starting city.

---

## Overview

The Traveling Salesman Problem (TSP) is a classic optimization problem. This script uses an Ant Colony Optimization (ACO) algorithm to approximate the shortest possible route. ACO is inspired by the behavior of ants searching for food, utilizing pheromone trails and heuristic information to find optimal solutions.

## Key Steps

1. **Input Data**: Define the coordinates of the cities.
2. **Distance Calculation**: Calculate the Euclidean distance between pairs of cities.
3. **Pheromone Initialization**: Initialize the pheromone matrix with a specified initial value.
4. **Heuristic Initialization**: Calculate the heuristic matrix based on the inverse distance between cities.
5. **Ant Colony Optimization**:
    - **Initialization**: Initialize parameters and data structures.
    - **Solution Construction**: Each ant constructs a tour based on pheromone trails and heuristic information.
    - **Pheromone Update**: Update pheromone levels based on the quality of the solutions found.
6. **Optimal Route Selection**: Select the tour with the shortest distance.

## Example Output

Best Distance: 220.23
Best Path: [0, 2, 3, 1]

---

This script provides an effective approach to solving the Traveling Salesman Problem by simulating the behavior of ants to explore and exploit possible routes over multiple iterations, gradually converging on an optimal solution.