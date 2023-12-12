from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        first = head

        while head:
            counter += 1
            head = head.next

        counter //= 2

        for i in range(counter):
            first = first.next

        return first
