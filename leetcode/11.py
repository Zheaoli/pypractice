# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 11.py
@time: 11:11
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max1 = 0
        while left < right and height[left] >= 0 and right <= len(height) - 1 and height[right] >= 0:
            max1 = max(max1, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max1
