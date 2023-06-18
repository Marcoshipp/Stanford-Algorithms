# uses adjacecy list to represent graph
import random
import copy
import math
graph = {}

with open("data.txt", 'r') as f:
    for line in f:
        line = line.strip()
        data = list(map(int, line.split("\t")))
        graph[data[0]] = data[1:]

class Graph:
    def __init__(self, g):
        self.graph = g
        self.original_nodes = len(g)
        self.nodes = [id + 1 for id in range(len(g))]
    def min_cut(self):
        while len(self.graph) != 2:
            self.contract()
        values = list(self.graph.values())
        return len(values[0])
    def contract(self):
        start = random.choice(self.nodes)
        chosen = random.choice(self.graph[start])
        self.graph[start].extend(self.graph.pop(chosen))
        self.nodes.remove(chosen)
        for lst in self.graph.values():
            for i, node in enumerate(lst):
                if node == chosen:
                    lst[i] = start

        # removing self cycles
        self.graph[start] = [id for id in self.graph[start] if id != start]
        return

class Test:
    def getMinCut(n):
        smallest = float("inf")
        for _ in range(n):
            g = Graph(copy.deepcopy(graph))
            mc = g.min_cut()
            if smallest > mc:
                smallest = mc
        return smallest
    
if __name__ == '__main__':
    print(Test.getMinCut(200))