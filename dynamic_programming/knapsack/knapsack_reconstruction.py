from dynamic_programming.knapsack.knapsack import knapsack


def knapsack_reconstruction(table, weights, values, n, capacity):
    solution = []
    c = capacity
    for i in range(n, 0, -1):
        if weights[i - 1] <= c and table[i - 1][c - weights[i - 1]] + values[i - 1] >= table[i - 1][c]:
            solution.append(i)
            c -= weights[i - 1]
    return solution


def read_data(path):
    f = open(path, "r")
    split_first_line = f.readline().rstrip().split(" ")
    values = []
    weights = []
    capacity = int(split_first_line[0])
    n = int(split_first_line[1])
    for _ in range(n):
        line = f.readline().rstrip().split(" ")
        values.append(int(line[0]))
        weights.append(int(line[1]))
    return {
        "values": values,
        "weights": weights,
        "capacity": capacity
    }


def main():
    data = read_data("../problem16.7test.txt")
    weights = data["weights"]
    values = data["values"]
    capacity = data["capacity"]
    n = len(values)
    table = knapsack(values, weights, capacity)
    print("Maximum profit is " + str(table[n][capacity]))
    print("Items picked are " + str(knapsack_reconstruction(table, weights, values, n, capacity)))


main()
