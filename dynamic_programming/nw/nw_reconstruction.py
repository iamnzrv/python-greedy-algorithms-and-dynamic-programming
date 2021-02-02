from dynamic_programming.nw.nw import nw


def nw_reconstruction(table, m, n, x, y, alpha_mismatch, alpha_gap):
    aligned_x = []
    aligned_y = []
    i = m
    j = n
    while i > 0 and j > 0:
        alpha = 0 if x[i - 1] == y[j - 1] else alpha_mismatch
        if table[i][j] == table[i - 1][j - 1] + alpha:
            aligned_x.append(x[i - 1])
            aligned_y.append(y[j - 1])
            i -= 1
            j -= 1
        elif table[i][j] == table[i - 1][j] + alpha_gap:
            aligned_x.append(x[i - 1])
            aligned_y.append('_')
            i -= 1
        elif table[i][j] == table[i][j - 1] + alpha_gap:
            aligned_x.append('_')
            aligned_y.append(y[j - 1])
            j -= 1
    return {
        "aligned_x": aligned_x,
        "aligned_y": aligned_y
    }


def read_data(path):
    f = open(path, "r")
    f.readline()
    gaps = f.readline().rstrip().split(" ")
    x = f.readline().rstrip()
    y = f.readline().rstrip()
    return {
        "alpha_gap": int(gaps[0]),
        "alpha_mismatch": int(gaps[1]),
        "x": x,
        "y": y
    }


def main():
    data = read_data("../problem17.8test.txt")
    res = nw(data["x"], data["y"], data["alpha_mismatch"], data["alpha_gap"])
    table = res["table"]
    m = res["m"]
    n = res["n"]
    print(table[m][n])
    aligned_sequences = nw_reconstruction(table, m, n, data["x"], data["y"], data["alpha_mismatch"], data["alpha_gap"])
    print(aligned_sequences["aligned_x"])
    print(aligned_sequences["aligned_y"])


main()
