# Traveling Salesman Problem Genetic Algorithm

This document demonstrates a solution to the Traveling Salesman Problem (TSP) using a genetic algorithm (GA). The goal is to find the shortest route that visits each city exactly once and returns to the starting city.

---

## Overview

The Traveling Salesman Problem (TSP) is a classic optimization problem. This script uses a genetic algorithm to approximate the shortest possible route. Genetic algorithms are inspired by natural selection, using mechanisms such as mutation, crossover, and selection to evolve better solutions over generations.

## Key Steps

1. **Input Data**: Define the coordinates of the cities.
2. **Distance Calculation**: Calculate the Euclidean distance between pairs of cities.
3. **Population Initialization**: Generate a population of random tours.
4. **Fitness Calculation**: Evaluate each tour based on the total distance.
5. **Selection**: Choose parents for the next generation based on their fitness scores.
6. **Crossover**: Create new tours by combining parts of parent tours.
7. **Mutation**: Introduce random changes to some tours to maintain genetic diversity.
8. **Generation Update**: Replace the old population with the new one.
9. **Optimal Route Selection**: After a set number of generations, select the tour with the shortest distance.

## Example Output
Best Distance: 220.23
Best Path: [0, 2, 3, 1, 0]

This script provides an effective approach to solving the Traveling Salesman Problem by evolving a population of routes over multiple generations to find an approximately optimal solution.
