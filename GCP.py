# !/usr/bin/python
# -*- coding: utf-8 -*-


res = 1


def gcp(graph, size_n, size_e):
    n = size_n
    head = [0] * (2 * size_e + 2)
    to = [0] * (2 * size_e + 2)
    next = [0] * (2 * size_e + 2)
    cnt_adj = 0
    # graph [x0,x1,x2] x0->x1 weight: x2
    for x in graph:
        cnt_adj += 1
        to[cnt_adj] = x[1]
        next[cnt_adj] = head[x[0]]
        head[x[0]] = cnt_adj
        cnt_adj += 1
        to[cnt_adj] = x[0]
        next[cnt_adj] = head[x[1]]
        head[x[1]] = cnt_adj
    vis = [0] * (n + 2)
    color = [0] * (n + 2)
    global res
    for i in range(1, n + 1):
        if not vis[i]:
            color[i] = 1
            dfs(i, color, vis, head, to, next)
    return res, color


def dfs(u, color, vis,  head, to, next):
    i = head[u]
    vis[u] = True
    global res
    while i:
        v = to[i]
        if not vis[v]:
            temp = [False] * (res + 3)
            j = head[v]
            while j:
                w = to[j]
                if vis[w]:
                    temp[color[w]] = True
                j = next[j]
            for i in range(1, res + 2):
                if not temp[i]:
                    color[v] = i
                    if i == res + 1:
                        res += 1
                    break
            dfs(v, color, vis,  head, to, next)
        i = next[i]


"""
n = 4
m = 5
graph = [[1, 2, 2],
         [1, 3, 2],
         [1, 4, 1],
         [2, 3, 5],
         [4, 3, 3]]
gcp(graph, n, m)
"""
