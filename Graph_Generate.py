
import random


class Edge:
    def __init__(self, x, y, w):
        # y is adjacent with x, and weight is w
        self.start = x
        self.to = y
        self.weight = w

    def __str__(self):
        return "%d %d %d" % (self.start, self.to, self.weight)

    @staticmethod
    def unweighted_edge(self):
        return "%d %d" % (self.start, self.to)


class Graph:
    def __init__(self, size_edge, directed=True):
        self.directed = directed
        self.edges = [[]for i in range(size_edge + 1)]

    def __str__(self):
        return self.generate()

    def generate(self, size_node, size_edge, weight=[1, 233], directed=True):
        res = []

        node = [1 for x in range(0, size_node + 1)]
        random.shuffle(node)
        node = eval([0] + node)
        edge = []

        random.shuffle(edge)
