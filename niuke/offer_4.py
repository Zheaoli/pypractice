# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: offer_4.py
@time: 22:31
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
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        return self.build(pre, tin, 0, len(pre) - 1, 0, len(tin) - 1)

    def build(self, pre, ins, pstart, pend, instart, inend):
        if pstart > pend:
            return None
        cur = pre[pstart]
        find = instart
        while find <= inend:
            if cur == ins[find]:
                break
            else:
                find += 1
        find = ins.find(cur)
        len = find - instart
        res = TreeNode(cur)
        res.left = self.build(pre, ins, pstart + 1, pstart + len, instart, find - 1)
        res.right = self.build(pre, ins, pstart + len + 1, pend, find + 1, inend)
        return res


        # write code here
