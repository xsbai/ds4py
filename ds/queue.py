# coding=utf-8
"""
基础数据结构
"""

# 队列
class Queue(object):

    #定义一个空队列
    def __init__(self,size):
        self.size = size  # 定义队列长度
        self.queue = []  # 存储队列 列表

    #队列(只能在队尾)添加一个元素
    def enqueue(self, item):
        # 入队
        if self.isFull():
            return -1
        self.queue.append(item)

    #删除队列（只能在对头）一个元素
    def dequeue(self):
        self.queue.pop(0)

    #判断队列是否为空
    def isEmpty(self):
        return(self.queue == [])

    #清空队列
    def clear(self):
        del(self.queue) #该队列就不存在了，而不是清空元素

    
    #返回队列项的数量
    def size(self):
        return(len(self.items))

    #打印队列
    def print(self):
        print(self.items)



# 定义循环队列类
class CircleQueue(Queue):
    def __init__(self, size):
        self.size = size  # 定义队列长度
        self.queue = []  # 存储队列 列表

    def __str__(self):
        # 返回对象的字符串表达式，方便查看
        return str(self.queue)

    def enqueue(self, n):
        # 入队
        if self.isFull():
            return -1
        self.queue.append(n)  # 列表末尾添加新的对象

    def dequeue(self):
        # 出队
        if self.isEmpty():
            return -1
        firstelement = self.queue[0]   # 删除队头元素
        self.queue.remove(firstelement)  # 删除队操作
        return firstelement

    def delete(self, n):
        # 删除某元素
        element = self.queue[n]
        self.queue.remove(element)

    def input(self, n, m):
        # 插入某元素 n代表列表当前的第n位元素 m代表传入的值
        self.queue[n] = m

    def getsize(self):
        # 获取当前长度
        return len(self.queue)

    def getnumber(self, n):
        # 获取某个元素
        element = self.queue[n]
        return element

    def isEmpty(self):
        # 判断是否为空
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self):
        # 判断队列是否满
        if len(self.queue) == self.size:
            return True
        return False