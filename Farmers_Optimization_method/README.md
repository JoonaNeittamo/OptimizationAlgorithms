# SAMK Advertisement Problem

This document illustrates the Farmers Optimization problem solved using Linear Programming (LP) with the PuLP library. The goal is to maximize audience reach for a marketing campaign while adhering to budget and advertising constraints.

## Key Steps:
1. **Problem Setup**: Define the optimization problem as a Linear Programming (LP) model named "Farmers Optimization" aiming to maximize audience reach.
2. **Variables Definition**: Declare decision variables representing the number of TV spots, newspaper ads, prime radio spots, and afternoon radio spots.
3. **Objective Function**: Formulate the objective function to maximize the total audience reached by assigning weights to each advertising medium.
4. **Constraints Setting**: Define constraints to ensure the budget is not exceeded, minimum radio spots requirements are met, and radio advertising costs are within the specified limit.
5. **Solving the LP Model**: Utilize the LP solver to find the optimal solution.
6. **Optimization Results**: Print the optimization status and the optimal allocation of resources, including the number of TV spots, newspaper ads, prime radio spots, afternoon radio spots, and the total audience reached.
7. **Execution Time**: Measure and display the time taken to solve the optimization problem.

---

## Example Output:
Optimization status: Optimal
TV Spots: 4.0
Newspaper Ads: 5.0
Prime Radio Spots: 18.0
Afternoon Radio Spots: 20.0
Total Audience Reached: 158800.0
Time: 0.056 seconds

This script demonstrates how Linear Programming can be applied to optimize resource allocation in marketing campaigns, ensuring maximum audience reach within budget constraints.