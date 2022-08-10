# https://leetcode.com/problems/reverse-linked-list/
# 67ms 15.4MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        node, prev = head, None
        # 들어온거(temp)를 마지막거(prev)에 붙이기
        while node:
            temp = node
            node = node.next
            temp.next = prev
            # 이전거 prev에 저장
            prev = temp
        return prev