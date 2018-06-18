# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Dijkstra
    optimize by FIB_Heap.
"""
import numpy as np

from Fib import Fib


def dijkstra(graph, size_n, size_e, s):
    n = size_n
    head = [0] * (2 * size_e + 2)
    to = [0] * (2 * size_e + 2)
    next = [0] * (2 * size_e + 2)
    weight = [0] * (2 * size_e + 2)
    cnt_adj = 0
    # graph [x0,x1,x2] x0->x1 weight: x2
    for x in graph:
        cnt_adj += 1
        to[cnt_adj] = x[1]
        weight[cnt_adj] = x[2]
        next[cnt_adj] = head[x[0]]
        head[x[0]] = cnt_adj
    vis = [False] * (n + 2)
    dis = [2147483647] * (n + 2)
    ret = [0] * (n + 2)
    dis[s] = 0
    ret[s] = s
    H = Fib(0, 0)
    H.Insert(0, s)
    while H.min != 0:
        minn = H.ExtractMin()
        u = minn.sta
        if(vis[u]):
            continue
        vis[u] = True
        i = head[u]
        while i:
            v = to[i]
            w = weight[i]
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                ret[v] = u
                H.Insert(dis[v], v)
            i = next[i]
    return dis, ret


"""
n = 4
m = 6
src = 1
graph = [[1, 2, 2], [2, 3, 2], [2, 4, 1], [1, 3, 5], [3, 4, 3], [1, 4, 4]]
dis = dijkstra(graph, n, m, src)
for x in range(1, n + 1):
    print(dis[x])
"""
"""
path = "io\\temp.txt"
fo = open(path, "r")
n, m = [int(x) for x in fo.readline().split()]
graph = []
for i in range(m):
    temp = [int(x) for x in fo.readline().split()]
    graph.append(temp)
fo.close()
src = 1
dis = dijkstra(graph, n, m, src)
for x in range(1, n + 1):
    print(dis[x])
"""
