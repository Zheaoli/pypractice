# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: xiaopang.py
@time: 23:44
"""
import re
import sys


def test():
    inp = sys.stdin
    line = inp.readline()
    while line:
        line = re.sub(r'\r\n|\n', '', line)
        a = re.findall(r'^([a-fA-F]).*$', line)
        while len(list(line)) > 0:

            if len(a) > 0 and ord(a[0]) < ord('f'):
                line = list(line)
                line.pop(0)
                line = ''.join(line)
                a = re.findall(r'^(' + a[0] + '|' + chr(ord(a[0]) + 1) + ').*$', line)
            else:
                print("数据错误")
                return None
    print("正确")


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

        pass

    @lazyproperty
    def area(self, value=0):
        print("Com")
        if value == 0 and self.radius == 0:
            raise TypeError("Something went wring")

        return math.pi * value * 2 if value != 0 else math.pi * self.radius * 2

    def test(self):
        pass


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
        a = type(self)(self.fget, fset, self.fdel, self.__doc__)
        return a

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class test():
    def __init__(self, value):
        self.value = value

    @Property
    def Value(self):
        return self.value

    @Value.setter
    def test(self, x):
        self.value = x


# test1=test()
# print(test1.value)
# test1.test=1


class meata(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
            return self._instance
        else:
            raise TypeError("fuck")


import weakref


class meta2(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if kwargs['name'] in self.__cache:
            return self.__cache[kwargs['name']]
        else:
            obj = super().__call__(*args, **kwargs)
            self.__cache[kwargs['name']] = obj
            return obj


# class li1(metaclass=meta2):
#     def __init__(self, name):
#         self._name = name
#
#
# class a1(metaclass=meata):
#     pass


# class a2(a1):
#     def test(self):
#         print('fuck')


class a3:
    @staticmethod
    def a():
        print(id(a3))

    @classmethod
    def c(cls):
        print(id(cls))


class zhe:
    a = 0


def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
            if "css_class" in kwds else ""

        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"

        return wrapped

    return real_decorator


def hello():
    return "Hello World"


tempdict1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'a',
    7: 'a'
}
import time


def test(*args, **kwargs):
    def func(test):
        test(*args, **kwargs)

    return func


class Timeit(object):
    def __init__(self, fun):
        self._wrapped = fun

    @test
    def __get__(self, instance, owner):
        return self.__call__(instance)

    def __call__(self, *args, **kwargs):
        def wraped(instance):
            start_time = time.time()
            result = self._wrapped(*args, **kwargs)
            print("fuckl1")
            return result

        return wraped


class Aj(object):
    @Timeit
    def func(self, pas):
        time.sleep(1)
        return "fyuck2" + str(pas)


class AX(object):
    def __call__(self, *args, **kwargs):
        print('from A')


class AL(object):
    x = 1
    gen = (lambda x: (x for _ in range(10)))(x)


print(list(AL.gen))

convert = lambda _dict: dict(i[::-1] for i in _dict.items())
print(convert(convert(tempdict1)))


class Grad(object):
    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.key] = value
        else:
            raise ValueError("fuck")

    def __set_name__(self, owner, name):
        self.key = name


class Exam(object):
    math1 = Grad()

    def __init__(self, math):
        self.math1 = math


class SingleMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        __new_o = cls.__new__

        # super().__init__(*args, **kwargs)

        def __new__(new, cls, *args, **kwargs):
            if cls._instance:
                return cls._instance
            cls._instance = cv = __new_o(new, *args, **kwargs)
            return cv

        cls.__new__ = __new__


class ANew(object, ):
    __metaclass__ = SingleMeta
    pass


class Des(object):
    pass


if __name__ == '__main__':
    # a = Aj()
    # print(a.func(1))
    # nicee1 = Exam(math=90)
    # print(nicee1.math1)
    # nice2 = Exam(math=60)
    # print(nice2.math1, nicee1.math1)
    # a = ANew()
    c = Circle(4)
    print(c.area)
    c.radius = 5
    print(c.area)
    c.area = 1
    pass
    # a = AX()
    # a()
    # a.__call__ = lambda: 'from lamba'
    # a.__call__()
    # a()
    # pass

    # fp = open("test.txt", "w+")
    # fp.write("a")
    # fp.close()
    # fp1 = open("test.txt", "a")
    # fp1.write("\nb\n")
    # fp1.close()
    # lix = li1(name='a')
    # li2 = li1(name='b')
    # print(id(lix))
    # print(id(li2))
    # zhe.a = 3
    # print(zhe.a)
    # c = Circle(4)
    # c.area
    # test = a2()
    # test.test()
    # test1 = a2()
    # test1.test()
