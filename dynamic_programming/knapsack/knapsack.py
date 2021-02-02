def knapsack(values, weights, capacity):
    n = len(values)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i - 1] <= j:
                table[i][j] = max(
                    values[i - 1] + table[i - 1][j - weights[i - 1]],
                    table[i - 1][j]
                )
            else:
                table[i][j] = table[i - 1][j]
    return table
