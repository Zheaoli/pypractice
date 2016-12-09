# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 15.py
@time: 14:46
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums:
            return result
        sortList = sorted(nums)
        for i in range(0, len(sortList)):
            if i != 0 and sortList[i] == sortList[i - 1]:
                continue
            target=-sortList[i]