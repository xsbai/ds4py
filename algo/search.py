# coding=utf-8
"""
基础查找算法
"""

class Search(object):
    
    # 二分查找
    def binary_chop(self, A, data):
        n = len(A)
        first = 0
        last = n - 1
        while first <= last:
            mid = (last + first) // 2
            if A[mid] > data:
                last = mid - 1
            elif A[mid] < data:
                first = mid + 1
            else:
                return mid
        return False

