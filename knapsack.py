# for more information, please visit: https://developers.google.com/optimization/bin/knapsack#python_1

# The following code imports the required libraries.
from ortools.algorithms import pywrapknapsack_solver


def main():
    # The following code declares the knapsack solver, a specialized solver for knapsack problems.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    # The code below creates the data for the problem.
    # The data includes the following:
    # weights: A list containing the weights of the items.
    # values: A list containing the values of the items.
    # capacities: A list with just one entry, the capacity of the knapsack.
    values = [18, 13, 23, 19, 16, 23, 33, 20, 20, 15, 37, 29, 27, 43, 13, 2]
    weights = [[10, 6, 13, 10, 15, 11, 15, 11, 9, 8, 18, 15, 13, 20, 7, 1]]
    capacities = [80]

    # The following code calls the solver and prints the solution.
    # The program first initializes the solver, and then calls it by computed_value = solver.Solve().
    # The total value of the optimal solution is computed_value, which is the same as the total weight in this case.
    # The program then gets the indices of the packed items in the solution as follows:
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()
    
    packed_items = []
    packed_weights = []
    total_weight = 0
    
    # Since solver.BestSolutionContains(i) returns TRUE if the item x is included in the solution,
    # packed_items is a list of the optimal packed items. Similarly, packed_weights are the weights of the packed items.
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]

    # add 1 to each index corresponding to the correct items packed.
    packed_items = [index + 1 for index in packed_items]

    print('Best value =', computed_value)
    print('Max weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed weights:', packed_weights)


if __name__ == '__main__':
    main()
