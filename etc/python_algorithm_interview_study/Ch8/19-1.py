# https://leetcode.com/problems/reverse-linked-list-ii/
# 55ms 14MB(책풀이)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
        # 예외처리
        if head is None or left == right:
            return head

        # start => 역순 연결리스트 시작전부분
        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next

        # 역순 연결리스트의끝의 다음값
        end = start.next

        # 뒤집기
        for _ in range(right - left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next

