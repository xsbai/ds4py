# coding=utf-8
"""
基础排序算法
"""

class Sort(object):
    def straight_insertion_sort(self, A):
        n = len(A)  # 序列A 的长度
        for i in range(1, n):  # 从序列A 的第二个元素开始比较。即下标从 1 开始。
            temp = A[i]  # 设置一个变量，承接当前的 元素的值
            j = i - 1  # 有序区的最后一个元素的索引，每次比较都是从和该位置元素比较开始，逐渐向左推进。
            while j >= 0 and temp < A[j]:  # j 指代 每个有序区元素的索引，所以j 不能小于0。 当 当前元素 小于 要比较的元素时，进行while循环。
                A[j + 1] = A[j]  # 将比当前元素大的有序区的元素向右移动一个位置。
                j -= 1  # 不着急放下当前元素，而是继续查看在j 元素之前是否还有元素，且该元素和当前元素相比，哪个大
            A[j + 1] = temp  # j前面已经没有元素了，或者是那个元素小于当前元素。那么将当前元素放到那个元素的后面。
        return A


    def binary_insertion_sort(self, A):
        n = len(A)
        for i in range(1, n):  # 无序区从1到n-1
            low = 0  # 初始化 low ，最开始为0
            high = i - 1  # 初始化 high ，最开始为 i-1 ，为有序区最大索引，
            temp = A[i]  # 定义一个变量，盛放无序区第一个元素，也就是要插入的元素
            while low <= high:  # 开始二分查找。注意 low <= high  这个条件
                mid = (low + high) // 2  # mid 是随着每次low或者是high的调整而动态调整的。防止出现小数，故使用地板除
                if temp < A[mid]:  # 如果 当前元素小于列表的中间元素
                    high = mid - 1  # 移动high到mid-1位置。 以下同理，移动low的位置。直到出现low>high情况，退出循环
                else:
                    low = mid + 1
            for j in range(i - 1, high, -1):  # 经过上述循环，找到要插入的位置即为high+1，因此从 i-1到high的元素向后移动
                A[j + 1] = A[j]
            A[high + 1] = temp  # 将当前元素放到相应位置。排序完成，返回序列。
        return A


    def shell_sort(self, A):
        n = len(A)
        step = n // 2  # 分组步长
        while step > 0:
            for i in range(0, n):  # 对分组数据进行插入排序
                if i + step < n:
                    temp = A[i]  # 先记下来每次大循环走到的第几个元素的值
                    if temp > A[i + step]:
                        A[i], A[i + step] = A[i + step], A[i] # 交换
            step = step // 2
        else:  # 最后一次，把基本排序好的数据再进行一次插入排序就好了
            for i in range(1, n):
                temp = A[i]  # 先记下来每次大循环走到的第几个元素的值
                j = i
                while j > 0 and A[j - 1] > temp:  # 当前元素的左边的紧靠的元素比它大,把左边的元素右移
                    A[j] = A[j - 1]  # 把左边的一个元素往右移一位
                    j -= 1  # 只一次左移只能把当前元素一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置为止
                A[j] = temp  # 已经找到了左边排序好的列表里不小于temp的元素的位置,把temp放在这里
        return A


    def bubble_sort(self, A):
        n = len(A)  # 计算列表元素有多少，从0开始算，所以填-1
        for i in range(n, 0, -1):  # 从后先前遍历
            for j in range(0, i-1):  # 从前向后遍历,最大到i，i之后的为有序
                if A[j] > A[j + 1]:  # 从前向后依次判断大小
                    A[j], A[j + 1] = A[j + 1], A[j]  # 交换
        return A


    def straight_select_sort(self, A):
        n = len(A)
        for i in range(0, n - 1):  # i为最左边第一个无序的数
            temp = i  # 保存进行交换的节点的下标
            for j in range(i + 1, n):  # 在i之后的数组里寻找
                if A[temp] > A[j]:  # 寻找最小的数
                    temp = j  # 保存最小数的下标
            if temp != i:
                A[temp], A[i] = A[i], A[temp]  # 进行交换
        return A


    def partitions(self, A, low, high):
        left = low
        right = high
        temp = A[left]  # 将最左侧的值赋值给temp
        while left < right:  # 当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
            while A[left] <= temp:  # 当left对应的值小于temp，就一直向右移动
                left += 1
            while A[right] > temp:  # 当right对应的值大于temp，就一直向左移动
                right = right - 1
            if left < right:
                A[left], A[right] = A[right], A[left]  # 若移动完，二者仍未相遇则交换下标对应的值
        A[low], A[right] = A[right], temp  # 若移动完，已经相遇，则交换right对应的值和temp
        return right  # 返回最右侧下标


    def quick_sort(self, A, low, high):  # 快排的主函数，传入参数为一个列表，左右两端的下标
        if high > low:
            k = self.partitions(A, low, high)  # 传入参数，通过Partitions函数，获取k下标值
            self.quick_sort(A, low, k - 1)  # 递归排序列表k下标左侧的列表
            self.quick_sort(A, k + 1, high)  # 递归排序列表k下标右侧的列表
        return A


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

