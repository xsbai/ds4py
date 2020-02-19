# coding=utf-8
"""
基础数据结构
"""

# 链表类
# 单节点类
class SingleListNode(object):
    def __init__(self, _item, _next=None):
        self.item = _item
        self.next = _next

# 双向节点类
class DoubleListNode(object):
    def __init__(self, _item, _prev=None, _next=None):
        self.item = _item
        self.prev = _prev
        self.next = _next

# 单链表类
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, newdata):
        node = SingleListNode(newdata, _next=self.head)
        self.head = node

    def append(self, newdata):
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, newdata):
        """将newdata插入pos位置之后"""
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = SingleListNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, olddata):
        """从单链表中删除所有的olddata"""
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == olddata:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next

    def length(self):
        """返回单链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        打印整个单链表
        return
        ls: list，从前至后的单链表
        """
        cur = self.head
        ls = []
        while cur is not None:
            ls.append(cur.item)
            cur = cur.next
        return ls

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.item == data:
                return True
            else:
                cur = cur.next
        return False

# 单向循环链表，继承单链表类
class SingleCircleLinkedList(SingleLinkedList):
    def __init__(self):
        self.head = None

    def add(self, newdata):
        """将新节点添加到单向循环链表头部。即头指针指向新节点，尾节点的指针指向新节点，新节点的指针指向原头节点"""
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node
            self.head = node

    def append(self, newdata):
        """与add方法唯一的区别为链表头的指针不变"""
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node

    def remove(self, olddata):
        """删除一个指定的节点"""
        cur = self.head
        pre = None
        if self.is_empty():
            return
        elif self.head.item == olddata:
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            pre = self.head
            while cur.next != self.head:
                if cur.item == olddata:
                    pre.next = cur.next
                    return
                pre = cur
                cur = cur.next
            if cur.item == olddata:
                pre.next = self.head

    def length(self):
        if self.is_empty():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.head
        ls = []
        while cur.next != self.head:
            ls.append(cur.item)
            cur = cur.next
        ls.append(cur.item)
        return ls

    def search(self, data):
        if self.is_empty():
            return False
        cur = self.head
        while cur.next != self.head:
            if cur.item == data:
                return True
            else:
                cur = cur.next
        if cur.item == data:
            return True
        return False

# 双向链表类，继承单链表类
class DoubleLinkedList(SingleLinkedList):
    def __init__(self):
        self.head = None

    def add(self, newdata):
        node = DoubleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, newdata):
        node = DoubleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, newdata):
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = DoubleListNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self, olddata):
        """删除一个指定的节点"""
        if self.is_empty():
            return
        elif self.head.item == olddata:
            if self.head.next is None:
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.item == olddata:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                    return
                cur = cur.next
            if cur.item == olddata:
                cur.prev.next = None

# 双向循环链表类
class DoubleCircleLinkedList(SingleCircleLinkedList):
    def __init__(self):
        self.head = None

    def add(self, newdata):
        node = DoubleListNode(newdata)
        if self.is_empty():
            self.head = node
            node.prev = node
            node.next = node
        else:
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
            self.head = node

    def append(self, newdata):
        node = DoubleListNode(newdata)
        if self.is_empty():
            self.head = node
            node.prev = node
            node.next = node
        else:
            self.head.prev.next = node
            self.head.prev = node
            node.prev = self.head.prev
            node.next = self.head

    def insert(self, pos, newdata):
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = DoubleListNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node

    def remove(self, olddata):
        if self.is_empty():
            return
        elif self.head.item == olddata:
            if self.length() == 1:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
        else:
            cur = self.head.next
            while cur != self.head:
                if cur.item == olddata:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.next
