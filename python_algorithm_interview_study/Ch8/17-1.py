# https://leetcode.com/problems/swap-nodes-in-pairs/
# 40ms 13.8MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def swapPairs(head: ListNode) -> ListNode:
        start = result = head
        while result and result.next:
            result.val, result.next.val = result.next.val, result.val
            result = result.next.next
        return start

