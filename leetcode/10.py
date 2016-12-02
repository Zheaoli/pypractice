# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 10.py
@time: 0:04
"""


class Solution(object):
    ResultCache = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0 and len(s) > 0:
            return False
        elif p == s:
            return True
        if (s, p) in self.ResultCache:
            return self.ResultCache[(s, p)]
        if len(p) == 1 or (len(p) > 0 and p[1] != "*"):
            self.ResultCache[(s[1:], p[1:])] = self.isMatch(s[1:], p[1:])
            return len(s) > 0 and (p[0] == '.' or s[0] == p[0]) and self.ResultCache[(s[1:], p[1:])]
        while s and (p[0] == '.' or s[0] == p[0]):
            self.ResultCache[(s, p[2:])] = self.isMatch(s, p[2:])
            if self.ResultCache[(s, p[2:])]:
                return True
            s = s[1:]
        self.ResultCache[(s, p[2:])] = self.isMatch(s, p[2:])
        return self.ResultCache[(s, p[2:])]


if __name__ == '__main__':
    a = Solution()
    print(a.isMatch("aab", "c*a*b"))
