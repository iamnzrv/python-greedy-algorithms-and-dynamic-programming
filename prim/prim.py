import time
from heapq import heapify, heappush, heappop


def get_minimum(visited, weights):
    minimum = float('inf')
    minimumIndex = -1
    for i in range(0, len(weights)):
        if weights[i] < minimum and visited[i] is False:
            minimum = weights[i]
            minimumIndex = i
    return minimumIndex


def prim_with_array_of_weights_implementation(graph):
    weights = [float('inf')] * len(graph)
    weights[0] = 0
    visited = [False] * len(graph)
    parents = [-1] * len(graph)
    parents[0] = -1
    for k in range(0, len(graph)):
        i = get_minimum(visited, weights)
        for j in range(0, len(graph)):
            if visited[j] is False:
                if graph[i][j] != 0 and graph[i][j] < weights[j] and parents[i] != j:
                    parents[j] = i
                    weights[j] = graph[i][j]
        visited[i] = True
    return parents

def prim_with_heap_of_weights_implementation(graph):
    heap = []
    heapify(heap)
    weights = [float('inf')] * len(graph)
    parents = [-1] * len(graph)
    visited = [False] * len(graph)
    visited[0] = True
    for i in range(0, len(graph)):
        if i != 0 and graph[0][i] != 0:
            weights[i] = graph[0][i]
            parents[i] = 0
        heappush(heap, (weights[i], i))
    while len(heap) > 0:
        winner = heappop(heap)
        heap.clear()
        visited[winner[1]] = True
        for j in range(len(graph)):
            if visited[j] is False:
                if graph[winner[1]][j] != 0 and graph[winner[1]][j] < weights[j]:
                    weights[j] = graph[winner[1]][j]
                    parents[j] = winner[1]
                heappush(heap, (weights[j], j))
    return parents


def getWay(g, parents):
    my_sum = 0
    for k in range(1, len(parents)):
        my_sum += g[k][parents[k]]
    return my_sum


test_graph = [
    [0, 4, 6, 0, 0, 0],
    [4, 0, 6, 3, 4, 0],
    [6, 6, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [0, 4, 0, 2, 0, 7],
    [0, 0, 0, 3, 7, 0]
]

g = []

f = open("../challenge15.9.txt", "r")
limits = f.readline().rstrip().split(" ")
size = int(limits[0])
for i in range(size):
    g.append([])
    for j in range(size):
        g[i].append(0)

for i in range(0, int(limits[1])):
    line = f.readline()
    data = list(map(lambda x: int(x), line.rstrip().split(" ")))
    g[data[0] - 1][data[1] - 1] = data[2]
    g[data[1] - 1][data[0] - 1] = data[2]

start = time.time()
res = prim_with_array_of_weights_implementation(g)
end = time.time()
print(res)
print(getWay(g, res))
print("Array implementation of Prim algorithm elapsed for " + str((end - start) * 1000) + "ms")
start = time.time()
res = prim_with_heap_of_weights_implementation(g)
end = time.time()
print(res)
print(getWay(g, res))
print("Heap implementation of Prim algorithm elapsed for " + str((end - start) * 1000) + "ms")
