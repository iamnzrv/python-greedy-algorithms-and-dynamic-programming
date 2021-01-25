import operator
import time


class DisjointSet(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, a):
        current = self.parent[a]
        while current != self.parent[current]:
            current = self.parent[current]
        return current

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]


def read_adjacency_lists(path):
    adjacency_lists = []
    f = open(path, "r")
    limits = f.readline().rstrip().split(" ")
    for _ in range(int(limits[1])):
        line = f.readline()
        data = list(map(lambda x: int(x), line.rstrip().split(" ")))
        data[0] -= 1
        data[1] -= 1
        adjacency_lists.append(data)
    return int(limits[0]), adjacency_lists


def kruskal(adjacency_lists, size):
    adjacency_lists = sorted(adjacency_lists, key=operator.itemgetter(2))
    ds = DisjointSet(size)
    mst_cost = 0
    for adjacency_list in adjacency_lists:
        if ds.find(adjacency_list[0]) != ds.find(adjacency_list[1]):
            ds.union(adjacency_list[0], adjacency_list[1])
            mst_cost += adjacency_list[2]
    return mst_cost


def main():
    read_data = read_adjacency_lists("../../challenge15.9.txt")
    adjacency_lists = read_data[1]
    size = read_data[0]
    start = time.time()
    mst_cost = kruskal(adjacency_lists, size)
    end = time.time()
    print("MST cost is " + str(mst_cost))
    print("Kruskal algorithm elapsed for " + str((end - start) * 1000) + "ms")


main()
