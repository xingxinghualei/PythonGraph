# !/usr/bin/python
# -*- coding: utf-8 -*-

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

    def generate(self, size_node, weight=[1, 233], directed=True):

        node = [1 for x in range(0, size_node + 1)]
        random.shuffle(node)
        node = [0] + node
        edge = []
        for x in self.edges:
            e = Edge(random.randint(1, size_node),
                     random.randint(1, size_node),
                     random.randint(weight[0], weight[1]))
            while e.to == e.start:
                e.to = random.randint(1, size_node)
            temp = [e.start, e.to, e.weight]
            edge.append(temp)
        random.shuffle(edge)

        return edge


"""
E = Edge(random.randint(1, 10), random.randint(
    1, 10), random.randint(2, 4))
print(E)

Test = Graph(10)
x = Test.generate(20, [1, 20], directed=False)
print(x)
"""
