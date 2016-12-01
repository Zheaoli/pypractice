# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: 2.py
@time: 10:57
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         tempList1 = []
#         tempList2 = []
#         tempresult = []
#         flag = False
#
#         while l1 is not None:
#             tempList1.append(l1.val)
#             l1 = l1.next
#         while l2 is not None:
#             tempList2.append(l2.val)
#             l2 = l2.next
#         if len(tempList1) > len(tempList2):
#             tempFlag = len(tempList1)
#         else:
#             tempFlag = len(tempList2)
#         for i in range(0, tempFlag):
#             if i >= len(tempList2):
#                 if flag is True:
#                     flag = False
#                     if (tempList1[i] + 1) >= 10:
#                         if i + 1 >= len(tempList1):
#                             tempresult.append((tempList1[i] + 1) % 10)
#                             tempresult.append(1)
#                         else:
#                             tempresult.append((tempList1[i] + 1) % 10)
#                             flag = True
#                     else:
#                         tempresult.append(tempList1[i] + 1)
#
#                 else:
#                     tempresult.append(tempList1[i])
#             elif i >= len(tempList1):
#                 if flag is True:
#                     flag = False
#                     if (tempList2[i] + 1) >= 10:
#                         if i + 1 >= len(tempList2):
#                             tempresult.append((tempList2[i] + 1) % 10)
#                             tempresult.append(1)
#                         else:
#                             tempresult.append((tempList2[i] + 1) % 10)
#                             flag = True
#                     else:
#                         tempresult.append(tempList2[i] + 1)
#
#                 else:
#                     tempresult.append(tempList2[i])
#             else:
#                 if flag is True:
#                     flag = False
#                     tempResult = tempList1[i] + tempList2[i] + 1
#                     if tempResult >= 10:
#                         if i + 1 >= len(tempList1):
#                             if i + 1 >= len(tempList2):
#                                 tempresult.append(tempResult % 10)
#                                 tempresult.append(1)
#
#                             else:
#                                 tempresult.append(tempResult % 10)
#                                 flag = True
#                         elif i + 1 >= len(tempList2):
#                             if i + 1 >= len(tempList1):
#                                 tempresult.append(tempResult % 10)
#                                 tempresult.append(1)
#
#                             else:
#                                 tempresult.append(tempResult % 10)
#                                 flag = True
#                         else:
#                             flag = True
#                             tempresult.append(tempResult % 10)
#                     else:
#                         tempresult.append(tempResult)
#                 else:
#                     if tempList1[i] + tempList2[i] >= 10:
#                         if i + 1 >= len(tempList1):
#                             if i + 1 >= len(tempList2):
#                                 tempresult.append((tempList1[i] + tempList2[i]) % 10)
#                                 tempresult.append(1)
#                                 flag = True
#                             else:
#                                 tempresult.append((tempList1[i] + tempList2[i]) % 10)
#                                 flag = True
#                         elif i + 1 >= len(tempList2):
#                             tempresult.append((tempList1[i] + tempList2[i]) % 10)
#                             flag = True
#                         else:
#                             tempresult.append((tempList1[i] + tempList2[i]) % 10)
#                             flag = True
#                     else:
#                         tempresult.append(tempList1[i] + tempList2[i])
#         tempNone = None
#         for z in range(0, len(tempresult)):
#             if z == 0:
#                 tempNone = ListNode(tempresult[z])
#             elif z == 1:
#                 tempNode = ListNode(tempresult[z])
#                 tempNone.next = tempNode
#             else:
#                 tempNode.next = ListNode(tempresult[z])
#                 tempNode = tempNode.next
#
#         return tempNone

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        listNode = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = listNode
        while p1 is not None or p2 is not None:
            if p1 is not None:
                carry += p1.val
                p1 = p1.next
            if p2 is not None:
                carry += p2.val
                p2 = p2.next
            p3.next = ListNode(carry % 10)
            p3 = p3.next
            carry /= 10
        if carry==1:
            p3.next=ListNode(1)
        return listNode.next


if __name__ == '__main__':
    b1 = ListNode(8)
    b2 = ListNode(6)
    a2 = ListNode(4)
    a1 = ListNode(6)
    a3 = ListNode(8)
    a1.next = a2
    b1.next = b2
    a2.next = a3
    a = Solution()
    a.addTwoNumbers(a1, b1)
