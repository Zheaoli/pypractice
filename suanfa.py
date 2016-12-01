# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: suanfa.py
@time: 17:22
"""
# from models import test


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    tempdict = {}
    if m == 0:
        for i in range(0, n):
            nums1[i] = nums2[i]
        return None
    if n == 0:
        return None
    for i in range(0, m):
        if (nums1[i] in tempdict) is False:
            tempdict[nums1[i]] = 1
        else:
            tempdict[nums1[i]] += 1
    for i in range(0, n):
        if (nums2[i] in tempdict) is False:
            tempdict[nums2[i]] = 1
        else:
            tempdict[nums2[i]] += 1
    # print(tempdict)
    del nums1[:]
    print(id(nums1))
    for i in tempdict.keys():
        nums1.append(i)


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


def enerate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    nums = [0] * numRows
    nums[0] = [1]
    nums[1] = [1, 1]
    for i in range(2, numRows):
        nums[i] = [0] * (i + 1)
        nums[i][0] = 1
        nums[i][i] = 1
        for j in range(1, i):
            nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
    return nums


# from models import test


class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class A:
    def __init__(self, ohms):
        self._ohms = ohms

    @Property
    def test(self):
        return self._ohms


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tempdict = {}
        if head is None:
            return None
        tempHead = head
        temp = head
        while tempHead is not None:
            if tempdict.has_key(temphead.value) is True:
                if tempdict[temphead.value] >= 1:
                    tempHead = self.removeNode(tempHead)
            else:
                tempdict[temphead.value] = 1
            tempHead = tempHead.next
        return head

    def removeNode(self, node):

        if node.next is not None:
            Next = node.next
            node.value = Next.value
            node.next = Next.value
            del Next
        else:
            return None

        return node


def countdown(n):
    print ("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):  # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


def generateList1(start, stop):
    for i in range(start, stop):
        yield i


def test(nums):
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] % 2 == 1:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                elif j == len(nums) - 1:
                    break


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        q = []
        if root is None:
            return result
        q.append(root)
        while len(q) > 0:
            vi = []
            i = 0
            n = len(q)
            while i < n:
                temp = q.pop(0)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                vi.append(temp.val)
                i += 1
            result.append(vi)
        result.reverse()
        return result


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    # text = "项目职务:性能测试 \n所在公司:成都育碧电脑软件有限公司 \n项目简介:基于UDP协议的项目主要是育碧的3A级别的项目,比如Watch Dogs,Rainbow 6 Siege,Just Dance等. \n项目职责:1. 和开发团队确定Test Schedule,测试环境(Load Test Environment),服务器配置(Server Configuration)以及其他技术细节\n2. 在Amazon EC2上准备测试机器,并使用育碧内部测试工具执行测试. \n3. 待测试完成,收集测试数据,比如Zabbix监控,Sever Logs,MySql Slow logs,Profiling Units和MySql Connections等. \n4. 对收集的测试数据进行分析,观察在测试的过程中,CCU(这里的判断标准为MySql Connections)是否达到并稳定在预期值.同时主要分析Server Logs,将Server Logs中的Error,Warning,Tracebacks用Python脚本获取他们基本的统计信息. \n5. 创建测试报告,描述在性能测试的过程中遇到的的问题,以及可能存在的瓶颈.和开发团队进行必要的沟通,如有相关优化,对项目进行验证测试. \n项目业绩:1. 搭建开源工具Logstash+Redis+Elasticsearch+Kibana对服务器Log和测试机Log进行实时分析.\n2. 基于Python创建Log分析工具分析服务器端的Log和测试机的Log. \n"
    # import re
    #
    # ref = re.compile(r"项目(.{2}):(.*?)(?=项目.{2})")
    # a = ref.match(text)
    # print(a)
    # b=Student("kasyss",98)
    # b.set_name="zy"
    # b.set_name('a')
    # c = u"12-14岁"
    # import re
    #
    # d = re.findall(ur'(?u)(\d{2}-\d{2})[\u4e00-\u9fa5]', c)
    # if d is not None:
    #     print(d)
    # c = countdown(5)
    # for i in c:
    #     print(i)
    #     if i == 5:
    #         j = c.send(3)
    #         pass


def countdown1(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = yield n
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1
c = countdown1(5)

for x in c:
    print(x)
    if x == 5:
        c.send(3)
    # nums = [1, 3, 4, 5, 8, 9, 11, 3, 41, 31, 88, 98];
    # test(nums)
    # print(nums)
    # a = generateList1(0, 5)
    # for c in range(0, 5):
    #     print(c)
    # # root=TreeNode(3)
    # # root.left=TreeNode(9)
    # # root.right=TreeNode(20)
    # # root.right.left=TreeNode(15)
    # # root.right.right=TreeNode(7)
    # # a=Solution()
    # # print(a.levelOrderBottom(root))
