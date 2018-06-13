# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Fibonacci Heap
"""


class FibNode:
    def __init__(self, key, sta):
        self.key = key
        self.sta = sta
        self.deg = 0
        self.p = 0
        self.c = 0
        self.le = 0
        self.r = 0
        self.marked = False

    # x.AddChild(y): y becomes x's child
    def AddChild(self, y):
        y.p = self
        self.deg = self.deg + 1
        if self.c == 0:
            self.child = y
            y.le = y
            y.r = y
        else:
            temp = self.c
            y.r = temp
            y.le = temp.le
            y.le.r = temp


class Fib:
    def __init__(self, n, minn):
        self.n = n
        self.min = minn

    def PrintRoot(self):
        z = self.min
        zle = self.min.le
        while True:
            print(" ( ", end="")
            print("%d-%d" % (int(z.key), int(z.deg)), end="")
            self.PrintNode(z)
            print(" ) ", end="")
            if(z == zle):
                break
            z = z.r

    def PrintNode(self, x):
        if(x.c != 0):
            z = x.c
            zle = x.c.le
            while True:
                print(" ( ", end="")
                print("%d-%d" % (int(z.key), int(z.deg)), end="")
                self.PrintNode(z)
                print(" ) ", end="")
                if(z == zle):
                    break
                z = z.r

    def Insert(self, key, sta):
        x = FibNode(key, sta)
        if self.min == 0:
            self.min = x
            x.le = x
            x.r = x
        else:
            x.r = self.min
            x.le = self.min.le
            x.le.r = x
            self.min.le = x
            if x.key < self.min.key:
                self.min = x
        self.n = self.n + 1

    def ExtractMin(self):
        z = self.min
        if z != 0:
            if z.c != 0:
                y = z.c
                while y.p != 0:
                    x = y.le
                    y.p = 0
                    y.le = 0
                    y.r = 0
                    y.r = self.min
                    y.le = self.min.le
                    y.le.r = y
                    self.min.le = y
                    y = x
            z.r.le = z.le
            z.le.r = z.r
            z.c = 0
            if z == z.r:
                self.min = 0
            else:
                self.min = z.r
                self.Consolidate()
            self.n = self.n - 1
        return z

    def Consolidate(self):
        A = [0] * 30
        z = self.min
        y = z.le
        while True:
            x = z
            d = z.deg
            while True:
                if A[d] == 0:
                    break
                p = A[d]
                if x.key > p.key:
                    temp = x
                    x = p
                    p = temp
                self.Link(p, x)
                A[d] = 0
                d = d + 1
            A[d] = x
            if z == y:
                break
            z = x.r

        self.min = 0
        for i in range(0, 28):
            if A[i] != 0:
                if self.min == 0:
                    self.min = A[i]
                    A[i].le = A[i]
                    A[i].r = A[i]
                else:
                    A[i].r = self.min
                    A[i].le = self.min.le
                    A[i].le.r = A[i]
                    self.min.le = A[i]
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def Link(self, y, x):
        y.r.le = y.le
        y.le.r = y.r
        y.p = x
        x.deg = x.deg + 1
        y.marked = False
        if x.c == 0:
            x.c = y
            y.le = y
            y.r = y
        else:
            z = x.c
            y.r = z
            y.le = z.le
            y.le.r = y
            z.le = y


"""
H = Fib(0, 0)
H.Insert(5384,0)
print(H.min.key)
H.ExtractMin()
H.Insert(4337,0)
H.Insert(291,0)
H.ExtractMin()
H.Insert(3776,0)
print(H.min.key)
H.Insert(2490,0)
H.Insert(3903,0)
H.ExtractMin()
H.Insert(5038,0)
H.Insert(4504,0)
H.PrintRoot()
"""
