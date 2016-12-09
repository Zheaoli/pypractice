# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 32.py
@time: 15:33
"""


# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) <= 0 or s is None:
#             return 0
#         Max = 0
#         stack = []
#         last = -1
#         for i in range(0, len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             elif s[i] == ')':
#                 if len(stack) == 0:
#                     last = i
#                 else:
#                     stack.pop()
#                     if len(stack) == 0:
#                         Max = max(Max, i - last)
#                     else:
#                         Max = max(Max, i - stack[-1])
#         return Max
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """



if __name__ == '__main__':
    a=Solution()
    print(a.longestValidParentheses("))))()()(("))