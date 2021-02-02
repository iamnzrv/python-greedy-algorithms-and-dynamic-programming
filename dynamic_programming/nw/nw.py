def nw(x, y, alpha_mismatch, alpha_gap):
    m = len(x)
    n = len(y)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        table[i][0] = i * alpha_gap
    for j in range(n + 1):
        table[0][j] = j * alpha_gap
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            alpha = 0 if x[i - 1] == y[j - 1] else alpha_mismatch
            table[i][j] = min(
                table[i - 1][j - 1] + alpha,
                table[i - 1][j] + alpha_gap,
                table[i][j - 1] + alpha_gap
            )
    return {
        "table": table,
        "m": m,
        "n": n
    }
