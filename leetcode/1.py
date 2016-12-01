# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 1.py
@time: 10:42
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        templist = []
        tempDict = {}
        for i in range(0, len(nums)):
            if nums[i] in tempDict:
                index=tempDict[nums[i]]
                templist.append(index)
                templist.append(i)
                return templist
            else:
                tempDict[target-nums[i]]=i

if __name__ == '__main__':
    s=Solution()
    print(s.twoSum([0,4,3,0],0))