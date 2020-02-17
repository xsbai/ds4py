# coding=utf-8
"""
基础数据结构
"""

"""
# 二叉树图形打印依赖
from graphviz import Digraph
import uuid
from random import sample
"""
# 栈类
class Stack(object):
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1

    def push(self,x):   # 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top=self.top+1

    def pop(self):  # 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top=self.top-1
            self.stack.pop()

    def isfull(self):
        return self.top+1 == self.size

    def isempty(self):
        return self.top == '-1'

    def showStack(self):
        print(self.stack)

# 队列类
class Queue(object):
    # 参考collections.deque
    pass

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


# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树
        #self.dot = Digraph(comment='Binary Tree')

    # 前序遍历
    def preorder(self):

        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 层序遍历
    def levelorder(self):

        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()
    """
    # 利用Graphviz实现二叉树的可视化
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

        # 绘制以某个节点为根节点的二叉树
        def print_node(node, node_tag):
            # 节点颜色
            color = sample(colors,1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())            # 左节点的数据
                self.dot.node(left_tag, str(node.left.data), style='filled', color=color)    # 左节点
                label_string = 'L' if label else ''    # 是否在连接线上写上标签，表明为左子树
                self.dot.edge(node_tag, left_tag, label=label_string)   # 左节点与其父节点的连线
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, str(node.right.data), style='filled', color=color)
                label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        # 如果树非空
        if self.data is not None:
            root_tag = str(uuid.uuid1())    # 根节点标签
            self.dot.node(root_tag, str(self.data), style='filled', color=sample(colors,1)[0])  # 创建根节点
            print_node(self, root_tag)

        self.dot.render(save_path)  # 保存文件为指定文件
    """


# 图类
class Graph(object):
    pass
