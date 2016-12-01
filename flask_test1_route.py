# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: flask_test1_route.py
@time: 14:34
"""
import time
from functools import wraps

import pymysql


class Test():
    def __init__(self):
        self.tempDict = {}

    def testDe(self, parterrn=None, func=None):
        def dec(func1):
            def test1():
                func1()

            return test1

        return dec

    def run(self):
        for i in self.tempDict.keys():
            self.tempDict[i]()


app = Test()


@app.testDe(parterrn='/')
def test():
    print('2')


def testDe1(func):
    def de(a, b, c):
        func(a, b, c)
        print('1')

    print('2')
    return de


@testDe1
def test2(a, b, c):
    print(a + b + c)


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        debug = kwargs.pop('debug', False)
        if debug:
            print('Calling ', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def a(x):
    print(x)


@optional_debug
def b(x, y):
    print(x + y)


@optional_debug
def c(x, y, z):
    print(x + y + z)


def time_cal(func):
    def run(*args, **kwargs):
        flag = time.time()
        func(*args, **kwargs)
        print(time.time() - flag)

    return run


@time_cal
def testTime(x):
    for i in range(0, x):
        if i == x - 1:
            print(i)


def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A(object):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(object):
    __metaclass__ = Singleton

    def __int__(self):
        print('Creating Spam')


from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expexted ' + str(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderedMetd(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
                d['_order'] = order
                return type.__new__(cls, clsname, bases, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()


def testCon():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='3550489', db='mysql', charset='UTF8')
    cur = conn.cursor()
    cur.execute("select version()")
    for i in cur:
        print(i)
    cur.close()
    conn.close()


class Person:
    def __init__(self):
        self._age = value

    def __int__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age must be a int')
        self._age = value


from abc import abstractmethod


class IStream():
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, *, debug=False, synchronize=False):
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        return super().__new__(cls, name, bases, ns)

    def __int__(self, name, bases, ns, *, debug=False, synchronize=False):
        super().__init__(name, bases, ns)


from inspect import signature
import logging


class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning("what fuck")


class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass


import inspect
import types


class MultiMehtod:
    def __int__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        sig = inspect.signature(meth)
        types = []
        for name, parm in sig.parameters.items():
            if name == 'self':
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(
                    'Argument {} must be annotated with a type'.format(name)
                )
            if not isinstance(parm.annotation, type):
                raise TypeError(
                    'Argument {} annotation must be a type'.format(name)
                )
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)
        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*arg)
        else:
            raise TypeError('No matching method for types {}'.format(types))

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class MultiDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            current_value = self[key]
            if isinstance(current_value, MultiMehtod):
                current_value.register(value)
            else:
                mvalue = MultiMehtod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    p = head
    pre = head
    while p is not None and p.next is not None:
        if p.next == head:
            return True
        p = p.next
        pre.next = head
        pre = p

    return False


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


if __name__ == '__main__':
    # a = ListNode(3)
    # b = ListNode(2)
    # c = ListNode(0)
    # d = ListNode(-4)
    # a.next = b
    # b.next = c
    # c.next = b
    #
    # hasCycle(a)
    print(func([1, 2, 3, 3, 3, 4, 5], [3, 3, 6, 7]))
