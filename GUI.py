# !/usr/bin/python
# -*- coding: utf-8 -*-

import re
from tkinter import *


class Label_1:
    def __init__(self, top):
        self.top = top
        self.lab = Label(top)

    def generate(self, text, row, column, justify=LEFT, padx=10):
        self.lab = Label(self.top,
                         text=text,
                         justify=justify,
                         padx=padx)
        self.grid(row, column)

    def grid(self, row, column):
        self.lab.grid(row=row,
                      column=column,
                      sticky=W)


class Entry_1:
    def __init__(self, top):
        self.top = top
        self.entry = Entry(top)

    def generate(self, var, row, column, width=15):
        self.entry = Entry(self.top,
                           width=width,
                           textvariable=var)
        self.grid(row, column)

    def grid(self, row, column):
        self.entry.grid(row=row,
                        column=column,
                        sticky=W)

    def extract(self):
        temp = self.entry.get()
        self.entry.delete(0, END)
        return temp


class Button_1:
    def __init__(self, top):
        self.top = top
        self.button = Button(top)

    def generate(self, text, cmd, row, column):
        self.button = Button(self.top,
                             text=text,
                             command=cmd)
        self.grid(row, column)

    def grid(self, row, column):
        self.button.grid(row=row,
                         column=column,
                         sticky=W)


top_op = Tk()
top_io = Tk()
top_mdzz = Tk()
top_mdzz.withdraw()
top_io.withdraw()
op_io = 3


def show_op(top_op, top_io, top_mdzz):
    top_op.update()
    top_op.deiconify()
    lx_op = Label_1(top_op)
    lx_op.generate("图的输入方式:\n1° 手动输入\n2° 文件输入\n0° 退出", 0, 1)
    lx_op.lab.grid(rowspan=3)
    lx_op_error = Label_1(top_op)
    lx_op_error.generate("", 3, 2)
    varOP = StringVar()
    varOP.set("2")
    ex_op = Entry_1(top_op)
    ex_op.generate(varOP, 0, 2)

    def getop():
        cmd = ex_op.extract()
        cmd = int(cmd)
        if cmd == 1:
            op_io = 1
            hide(top_op)
            show_mdzz(top_op, top_io, top_mdzz)
            return op_io
        elif cmd == 2:
            op_io = 2
            hide(top_op)
            show_io(top_op, top_io, top_mdzz)
            return op_io
        elif cmd == 0:
            exit(0)
        else:
            lx_op_error.lab["text"] = "请输入1或2或0"
            lx_op_error.lab["bg"] = "red"

    bx_op = Button_1(top_op)
    bx_op.generate("确认选择", getop, 1, 2)

    top_op.mainloop()


def show_io(top_op, top_io, top_mdzz):
    top_io.update()
    top_io.deiconify()
    lx_io = Label_1(top_io)
    lx_io.generate("文件(绝对)路径: \nWindows系统下,以\\分隔\nUnix下以/分隔", 0, 1)
    varIO = StringVar()
    ex_io = Entry_1(top_io)
    ex_io.generate(varIO, 1, 1)
    ex_io.entry.grid(sticky=W)
    ex_io.entry.insert(END, "io\\indata1.txt")

    def sure_1():
        class LastCharacterError(Exception):
            def __init__(self):
                Exception.__init__(self)
        path = ex_io.extract()
        try:
            if path == "" or path[-3:] != "txt":
                raise LastCharacterError
        except FileNotFoundError:
            print("运行错误：请检查文件目录(path变量)是否正确！")
            exit(1)
        except LastCharacterError:
            print("请输入txt文档")
            exit(1)
        hide(top_io)

    def back_1():
        hide(top_io)
        show_op(top_op, top_io, top_mdzz)
    bx_1 = Button_1(top_io)
    bx_1.generate("确认", sure_1, 4, 1)
    bx_2 = Button_1(top_io)
    bx_2.generate("返回", back_1, 4, 2)
    top_io.mainloop()


def show_mdzz(top_op, top_io, top_mdzz):
    top_mdzz.update()
    top_mdzz.deiconify()
    lx_v = Label_1(top_mdzz)
    lx_v.generate("顶点数", 0, 1)
    varV = StringVar()
    ex_v = Entry_1(top_mdzz)
    ex_v.generate(varV, 0, 2)
    lx_e = Label_1(top_mdzz)
    lx_e.generate("边数", 1, 1)
    varE = StringVar()
    ex_e = Entry_1(top_mdzz)
    ex_e.generate(varE, 1, 2)
    lx_sb = Label_1(top_mdzz)
    lx_sb.generate("输入边 v u w\nu邻接于v，权重为w\n用\'.\'作为间隔", 2, 1)
    varEdges = StringVar()
    ex_sb = Entry_1(top_mdzz)
    ex_sb.generate(varEdges, 5, 1)
    ex_sb_s = Scrollbar(top_mdzz, orient="horizontal")
    ex_sb_s.grid(row=6,
                 column=1,
                 ipadx=12)
    ex_sb_s.config(command=ex_sb.entry.xview)
    ex_sb.entry.config(xscrollcommand=ex_sb_s.set)
    lx_mdzz_error = Label_1(top_mdzz)
    lx_mdzz_error.generate("", 3, 2)

    def sure_1():
        ver = ex_v.entry.get()
        es = ex_e.entry.get()
        edg = ex_sb.entry.get()
        edges = re.split(r"\.+", edg)
        judge = True
        if(len(edges) != int(es)):
            lx_mdzz_error.lab["text"] = "边数量不符合\n期望:%s 实际:%d" % (
                es, len(edges))
            lx_mdzz_error.lab["bg"] = "red"
            judge = False
        for i in range(len(edges)):
            temp = edges[i].split()
            if(len(temp) != 3):
                lx_mdzz_error.lab["text"] = "第%d条边缺少参数" % (i + 1)
                lx_mdzz_error.lab["bg"] = "red"
                judge = False
                break
            elif not (1 <= int(temp[0]) <= int(ver) and 1 <= int(temp[1]) <= int(ver)):
                lx_mdzz_error.lab["text"] = "第%d条边顶点错误" % (i + 1)
                lx_mdzz_error.lab["bg"] = "red"
                judge = False
                break

        if(judge):
            fo = open("io\\temp.txt", "w")
            fo.write(ver + " " + es + "\n")
            for x in edges:
                for y in x.split():
                    fo.write(y + " ")
                fo.write("\n")
            fo.close()

    def back_1():
        hide(top_mdzz)
        show_op(top_op, top_io, top_mdzz)
    bx_1 = Button_1(top_mdzz)
    bx_1.generate("确认", sure_1, 7, 1)
    bx_2 = Button_1(top_mdzz)
    bx_2.generate("返回", back_1, 7, 2)
    top_mdzz.mainloop()


def hide(top):
    top.withdraw()


show_op(top_op, top_io, top_mdzz)

"""
lx_io = Label_1(top)
lx_io.generate("文件(绝对)路径: ", 0, 1)
varIO = StringVar()
varIO.set("io\\indata1.txt")
ex_io = Entry_1(top)
ex_io.generate(varIO, 0, 2)
"""
