# coding=utf-8
"""
基础数据结构测试类
"""
from ds4py import SingleLinkedList,SingleCircleLinkedList,DoubleLinkedList,DoubleCircleLinkedList
from ds4py import BTree
from ds4py import Stack
class test_stack:
    def test_stack(self):
        s=Stack(10)
        for i in range(6):
            s.push(i)
        s.showStack()
        for i in range(3):
            s.pop()
        s.showStack()

class test_link:
    def __init__(self):
        pass
    
    # 单链表测试
    def test_SL(self):
        SL = SingleLinkedList()
        print('单链表是否为空：', SL.is_empty())
        SL.add(1)
        SL.add(2)
        SL.append(5)
        print('单链表为：', SL.travel())
        SL.insert(2, 3)
        print('单链表中是否有4：', SL.search(4))
        print('单链表为：', SL.travel())
        print('单链表长度：', SL.length())
        SL.remove(2)
        print('单链表为：', SL.travel())
    
    # 单循环链表测试
    def test_SCL(self):
        SCL = SingleCircleLinkedList()
        print('单循环链表是否为空：', SCL.is_empty())
        SCL.add(1)
        SCL.add(2)
        SCL.append(5)
        print('单循环链表为：', SCL.travel())
        print("在第二个节点之后插入节点'3'")
        SCL.insert(2, 3)
        print('单循环链表为：', SCL.travel())
        print('单循环链表中是否有4：', SCL.search(4))
        print('单循环链表长度：', SCL.length())
        print("删除节点'5'")
        SCL.remove(5)
        print('单循环链表为：', SCL.travel())

    # 双向链表测试
    def test_DL(self):
        DL = DoubleLinkedList()
        print('双向链表是否为空：', DL.is_empty())
        DL.add(1)
        DL.add(2)
        DL.append(5)
        print('双向链表为：', DL.travel())
        print("在第二个节点之后插入节点'3'")
        DL.insert(2, 3)
        print('双向链表为：', DL.travel())
        print('双向链表中是否有4：', DL.search(4))
        print('双向链表长度：', DL.length())
        print("删除节点'1'")
        DL.remove(1)
        print('双向链表为：', DL.travel())

    # 双向循环链表测试
    def test_DCL(self):
        DCL = DoubleCircleLinkedList()
        print('双向循环链表是否为空：', DCL.is_empty())
        DCL.add(1)
        DCL.add(2)
        DCL.append(5)
        print('双向循环链表为：', DCL.travel())
        print("在第二个节点之后插入节点'3'")
        DCL.insert(2, 3)
        print('双向循环链表为：', DCL.travel())
        print('双向循环链表中是否有10：', DCL.search(10))
        print('双向循环链表长度：', DCL.length())
        print("删除节点'1'")
        DCL.remove(1)
        print('双向循环链表为：', DCL.travel())


class test_btree:
    def __init__(self):
        pass

    # 手动构造二叉树, BOTTOM-UP METHOD
    def create_tree(self): 
        right_tree = BTree(6)
        right_tree.left = BTree(2)
        right_tree.right = BTree(4)

        left_tree = BTree(5)
        left_tree.left = BTree(1)
        left_tree.right = BTree(3)

        tree = BTree(11)
        tree.left = left_tree
        tree.right = right_tree

        left_tree = BTree(7)
        left_tree.left = BTree(3)
        left_tree.right = BTree(4)

        right_tree = tree # 增加新的变量
        tree = BTree(18)
        tree.left = left_tree
        tree.right = right_tree

        return tree

    # 利用列表构造二叉树
    # 列表中至少有一个元素
    def create_tree_by_list(self,array):

        i = 1
        # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
        level_order = []
        sum = 1

        while sum < len(array):
            level_order.append(array[i-1:2*i-1])
            i *= 2
            sum += i
        level_order.append(array[i-1:])

        # BTree_list: 这一层所有的节点组成的列表
        # forword_level: 上一层节点的数据组成的列表
        def Create_BTree_One_Step_Up(BTree_list, forword_level):

            new_BTree_list = []
            i = 0
            for elem in forword_level:
                root = BTree(elem)
                if 2*i < len(BTree_list):
                    root.left = BTree_list[2*i]
                if 2*i+1 < len(BTree_list):
                    root.right = BTree_list[2*i+1]
                new_BTree_list.append(root)
                i += 1

            return new_BTree_list

        # 如果只有一个节点
        if len(level_order) == 1:
            return BTree(level_order[0][0])
        else: # 二叉树的层数大于1
            # 创建最后一层的节点列表
            BTree_list = [BTree(elem) for elem in level_order[-1]]

            # 从下往上，逐层创建二叉树
            for i in range(len(level_order)-2, -1, -1):
                BTree_list = Create_BTree_One_Step_Up(BTree_list, level_order[i])

            return BTree_list[0]
    
    def test_create_tree_by_list(self):
        array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tree = self.create_tree_by_list(array)
        return tree

    def test_tree(self,tree):
        print('先序遍历为:')
        tree.preorder()

        print('\n中序遍历为:')
        tree.inorder()

        print('\n后序遍历为:')
        tree.postorder()

        print('\n层序遍历为:')
        level_order = tree.levelorder()
        print(level_order)

        print('叶子节点为:')
        tree.leaves()

        height = tree.height()
        print('\n树的高度: %s.' % height)

        # 利用Graphviz进行二叉树的可视化
        # tree.print_tree(save_path='E://create_btree_by_list.gv', label=True)

if __name__ == '__main__':
    # 堆栈测试
    stack = test_stack()
    stack.test_stack()

    # 链表测试
    link = test_link()
    # link.test_DCL()

    # 二叉树测试
    tree_object = test_btree()
    # tree = tree_object.test_create_tree_by_list()
    # tree = tree_object.create_tree()
    # tree_object.test_tree(tree)

    