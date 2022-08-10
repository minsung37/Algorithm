# https://leetcode.com/problems/odd-even-linked-list/
# 61ms 16.6MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def oddEvenList(head: ListNode) -> ListNode:
        # 예외처리
        if head is None:
            return None
        odd = head
        even_head = even = head.next

        # 135... 24... 연결
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드 뒤에 짝수 붙이기
        odd.next = even_head
        return head