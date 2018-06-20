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


def gcp2(graph, size_n, size_e):
    n = size_n
    map = [[0] * (n + 2) for i in range(n + 1)]
    deg = [[i + 1, 0, 0]for i in range(0, n + 1)]
    cnt_adj = 0
    # graph [x0,x1,x2] x0->x1 weight: x2
    for x in graph:
        map[x[0]][x[1]] = map[x[1]][x[0]] = True
        deg[x[0] - 1][1] += 1
        deg[x[1] - 1][1] += 1
    f = sorted(deg, key=lambda x: x[1], reverse=True)
    res2 = 0
    tot = 0
    while tot < n:
        res2 += 1
        for i in range(1, n + 1):
            if f[i - 1][2] != 0:
                continue
            ok = True
            for j in range(1, n + 1):
                if map[f[i - 1][0]][f[j - 1][0]] == 0:
                    continue
                if f[j - 1][2] == res2:
                    ok = False
                    break
            if ok == 0:
                continue
            f[i - 1][2] = res2
            tot += 1

    f = sorted(f, key=lambda x: x[0],)
    return res2, [0] + [x[2] for x in f]


if __name__ == '__main__':
    n = 4
    m = 5
    graph = [[1, 2, 2],
             [1, 3, 2],
             [1, 4, 1],
             [2, 3, 5],
             [4, 3, 3]]
    ans, li = gcp2(graph, n, m)
    print(ans, li)
