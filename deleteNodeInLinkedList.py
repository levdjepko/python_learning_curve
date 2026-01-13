# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/553/
# Definition of a singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void. Do not return anything; modify the node in-place instead.
        """
        # look at the next node
        # and make our node a copy of the next node
        nextNode = node.next
        
        
        node.val = nextNode.val
        node.next = nextNode.next
