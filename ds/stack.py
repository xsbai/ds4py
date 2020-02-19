# coding=utf-8
"""
基础数据结构
"""

# 栈类
class Stack(object):
    def __init__(self,_size):
        self.size = _size
        self.stack = []
        self.top = -1

    def push(self,x):   # 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top = self.top+1

    def pop(self):  # 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top = self.top-1
            self.stack.pop()

    def isfull(self):
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == '-1'

    def showStack(self):
        print(self.stack)
