# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 31.py
@time: 14:01
"""


#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)
        pivot = right - 1
        sucessor = 0
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                sucessor = i
                break
        nums[pivot], nums[sucessor] = nums[sucessor], nums[pivot]
        self.reverse(nums, pivot + 1, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[i]
            l += 1
            r -= 1
