from dynamic_programming.wis.wis import wis


def wis_reconstruction(arr, weighted_list):
    reconstructed_set = []
    i = len(arr) - 1
    while i >= 2:
        if arr[i - 1] >= arr[i - 2] + weighted_list[i - 1]:
            i -= 1
        else:
            reconstructed_set.append(i)
            i -= 2
    if i == 1:
        reconstructed_set.append(i)
    reconstructed_set.reverse()
    return reconstructed_set


def read_weighted_list(path):
    weighted_list = []
    f = open(path, "r")
    size = int(f.readline().rstrip().split(" ")[0])
    for _ in range(size):
        weighted_node = int(f.readline().rstrip().split(" ")[0])
        weighted_list.append(weighted_node)
    return weighted_list


def main():
    weighted_list = read_weighted_list("../challenge16.6.txt")
    arr = wis(weighted_list)
    res = wis_reconstruction(arr, weighted_list)
    print("Maximum sum of weights is " + str(arr[len(arr) - 1]))
    print("WSIT is " + str(res))


main()
