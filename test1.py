# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: test1.py
@time: 15:46
"""


def func(num1, num2):
    tempdict = {}
    temp = []
    for i in num1:
        if tempdict.has_key(i):
            tempdict[i] += 1
        else:
            tempdict[i] = 1
    for i in tempdict.keys():
        if tempdict[i] != 1:
            value = tempdict[i]
            tempdict[i] = {'value': value, 'count': value}
    for i in num2:
        if tempdict.has_key(i):
            if isinstance(tempdict[i], dict):
                tempdict[i]['count'] -= 1
            else:
                tempdict[i] -= 1
    for i in tempdict.keys():
        if isinstance(tempdict[i], int):
            if tempdict[i] == 0:
                temp.append(i)
        elif isinstance(tempdict[i], dict):
            temprange = tempdict[i]['value'] - tempdict[i]['count']
            for j in range(0, temprange):
                temp.append(i)
    return temp


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class A:
    pass


# class Property1(object):
#    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#        self.fget = fget
#        self.fset = fset
#        self.fdel = fdel
#        self.__doc__ = doc

#    def __get__(self, instance, owner=None):
#        print(instance)
#        print(self.fget)
#        if instance is None:
#            return self
#        if self.fget is None:
#            raise AttributeError("Unreadable attribute")
#        return self.fget(instance)

#    def __set__(self, obj, value):
#        if self.fset is None:
#            raise AttributeError, "can't set attribute"
#        self.fset(obj, value)

#    def __delete__(self, obj)#:
#        if self.fdel is None:
#            raise AttributeError, "can't delete attribute"
#        self.fdel(obj)


def test1(nums):
    temp = {}
    if nums is None:
        return None
    for i in nums:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    min = len(nums) - 1
    for i in temp.keys():
        if temp[i] == 1:
            if nums.index(i) < min:
                min = nums.index(i)
    return nums[min]


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print("getattr:", item)
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('setattr:', key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


def recvfrom(*args, **kwargs):
    pass
    return (a, b)


from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


def grep(pattern):
    print('Looking for %s' % pattern)
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('fuck')


def countdown(n):
    print('Counting down from %s', n)
    while n >= 0:
        newvalue = yield n
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


class Node:
    pass


import types


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    a = last.send(last_result)
                    stack.append(a)
                    # stack.append()
                    last_result = None
                elif isinstance(last, Node):
                    temp = stack.pop()
                    temp2 = self._visit(temp)
                    stack.append(temp2)
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_', +type(node).__name__))


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        a = yield node.left
        b = yield node.right
        yield a - b
        # yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (node.left) * (node.right)

    def visit_Div(self, node):
        yield (node.left) / (node.right)

    def visit_Negate(self, node):
        yield -(node.operand)


def testx():
    for i in range(1, 10):
        x = yield i
        print(x)


import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name


def get_spam(name):
    return Spam.manager.get_spam(name)


class ClassMethod(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, kclass=None):
        if kclass is None:
            kclass = type(obj)

        def newfunc(*args):
            return self.f(kclass, *args)

        return newfunc


class A1(object):
    @ClassMethod
    def print1(cls, a=None):
        print(a)


#class Property(onject):
#    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#        self.fget = fget
#        self.fset = fset
#        self.fdel = fdel
#        if doc is None and fget is not None:
#            doc = fget.__doc__
#        self.__doc__ = doc
#
#    def __get__(self, obj, objtype=None):
#        if obj is None:
#            return self
#        if self.fget is None:
#            raise AttributeError("unreadable attribute")
#        return self.fget(obj)
#
#    def __set__(self, obj, value):
#        if self.fset is None:
#            raise AttributeError("can`t set attribute")
#        self.fset(obj, value)
#
#    def __delete__(self, instance):
#        if self.fdel is None:
#            raise AttributeError("Can`t delete attribute")
#        self.fdel(obj)

class MyBaseClass(object):
    def __init__(self,value):
        self.value=value
class TimesFive(MyBaseClass):
    def __init__(self,value):
        MyBaseClass.__init__(self,value)
        self.value*=5
class PlusTwo(MyBaseClass):
    def __init__(self,value):
        MyBaseClass.__init__(self,value)
        self.value+=2
class ThisWay(TimesFive,PlusTwo):
    def __init__(self,value):
        super(ThisWay,self).__init__(value)
class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    def _traverse_dict(self,instance_dict):
        output={}
        for key,value in instance_dict.items():
            output[key]=self._traverse(key,value)
        return output
    def _traverse(self,key,value):
        if isinstance(value,ToDictMixin):
            return value.to_dict()
        elif isinstance(value,dict):
            return self._traverse_dict(value)
        elif isinstance(value,list):
            return [self._traverse(key,i)for i in value]
        elif hasattr(value,'__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value
class BinaryTree(ToDictMixin):
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right




if __name__ == '__main__':
    # a = ListNode(3)
    # b = ListNode(2)
    # c = ListNode(0)
    # d = ListNode(-4)
    # a.next = b
    # b.next = c
    # c.next = b
    tree=BinaryTree(10,left=BinaryTree(7,right=BinaryTree(9)),right=BinaryTree(13,left=BinaryTree(11)))
    print(tree.to_dict())
    # hasCycle(a)
    # a = Number(0)
    # for n in range(1, 100000):
    #     a = Add(a, Number(n))
    # e = Evaluator()
    # print(e.visit(a))
    # t1 = Sub(Number(3), Number(4))
    # b = Evaluator()
    # b.visit(t1)
    # print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
    # a = get_spam("foo")
    #A1.print1()
    # a = testx()
    # print(a.send(None))
    # print(a.send(('a')))
