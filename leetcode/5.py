# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 5.py
@time: 15:03
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        lognest = s[0:1]
        for i in range(0, len(s)):
            tmp = self.str_helper(s, i, i)
            if len(tmp) > len(lognest):
                lognest = tmp
            tmp = self.str_helper(s, i, i + 1)
            if len(tmp) > len(lognest):
                lognest = tmp
        return lognest

    def str_helper(self, s1, left, right):
        n = len(s1)
        while left >= 0 and right <= n - 1 and s1[left] == s1[right]:
            left -= 1
            right += 1
        return s1[left + 1:right]


if __name__ == '__main__':
    a = Solution()
    print(a.longestPalindrome('babad'))
