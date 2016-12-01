# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: a.py
@time: 23:38
"""


class Grade(object):
    def __init__(self):
        self._score = 0

    def __get__(self, instance, owner):
        return self._score

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError('grade must be between 0 and 100')


class Exam(object):
    math = Grade()

    def __init__(self, math):
        self.math = math

    def generator():
        for i in range(10):
            yield i
        for j in range(10, 20):
            yield j


def generator2():
    for i in range(10):
        yield i


def generator3():
    for j in range(10, 20):
        yield
    for v in g:
        yield v


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    tempList = nums1 + nums2
    tempList = sorted(tempList)
    if len(tempList) % 2 == 0:
        return float(tempList[len(tempList) / 2 - 1] + tempList[len(tempList) / 2]) / 2
    else:
        return tempList[int(len(tempList))]


# type(a).__dict__['x'].__get__(Exam, None)
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name1(self):
        return 100
    full_name2=property(full_name1)

    def __call__(self, *args, **kwargs):
        print("call function")


if __name__ == '__main__':
    person = Person("a", "b")
    setattr(person, fu, "test")
    print(person.full_name)
    # findMedianSortedArrays([1,2],[3,4])
    # niche = Exam(math=90)
    # print(niche.math)
    # # output : 90
    # snake = Exam(math=75)
    # print(snake.math)
    # # output : 75
    # # snake.math = 120
    # print(niche.math)

    # output: ValueError:grade must be between 0 and 100!
