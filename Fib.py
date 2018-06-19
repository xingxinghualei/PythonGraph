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


class Fib:
    def __init__(self, n, minn):
        self.n = n
        self.min = minn

    def PrintRoot(self):
        """
        print all node in Fibonacci
        use bracket to divide the depth
        and display the node depth
        """
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
        """
            Create a node with key and satellite data
            Insert the node into root list
        """
        x = FibNode(key, sta)
        if self.min == 0:
            self.min = x
            x.le = x
            x.r = x
        else:
            self.AddNode(x, self.min)
            if x.key < self.min.key:
                self.min = x
        self.n = self.n + 1

    def ExtractMin(self):
        z = self.min
        if z != 0:
            while z.c != 0:
            """
                remove z's children to root list
            """
                x = z.c
                self.RemoveNode(x)
                if x == x.r:
                    z.c = 0
                else:
                    z.c = x.r
                self.AddNode(x, z)  # add x to root list
                x.p = 0
            self.RemoveNode(z)
            z.c = 0
            if z == z.r:
                self.min = 0
            else:
                self.min = z.r
                self.Consolidate()
            self.n = self.n - 1
        return z

    def Consolidate(self):
        """
            merge same degree node in the root list
            D(n) <= [log(n)/log((√5+1)/2)]. Taking 10 as base
        """
        A = [0] * 30
        # consolidate same degree node
        while self.min != 0:
            """
                Traverse root list
                it works by removing every node in root list
            """
            x = self.RemoveMinNode()
            d = x.deg
            while A[d] != 0:
                p = A[d]
                if x.key > p.key:   # maintain Min-Heap structure
                    temp = x
                    x = p
                    p = temp
                self.Link(p, x)
                A[d] = 0
                d = d + 1
            A[d] = x
        self.min = 0

        # add removed node to root list
        for i in range(0, 28):
            if A[i] != 0:
                if self.min == 0:
                    self.min = A[i]
                    A[i].le = A[i]
                    A[i].r = A[i]
                else:
                    self.AddNode(A[i], self.min)
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def Link(self, y, x):
        """
            make y become x's children
        """
        self.RemoveNode(y)
        if x.c == 0:
            x.c = y
        else:
            self.AddNode(y, x.c)
        y.p = x
        x.deg = x.deg + 1
        y.marked = False

    def AddNode(self, y, x):
        """
            add y on the x's left
            a<-->x ==> a<-->y<-->x
        """
        y.le = x.le
        y.r = x
        x.le.r = y
        x.le = y

    def RemoveNode(self, x):
        x.r.le = x.le
        x.le.r = x.r

    def RemoveMinNode(self):
        minn = self.min
        if minn == minn.r:
            self.min = 0
        else:
            self.RemoveNode(minn)
            self.min = minn.r
        minn.le = minn.r = minn
        return minn


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
