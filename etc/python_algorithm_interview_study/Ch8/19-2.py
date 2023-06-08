# https://leetcode.com/problems/reverse-linked-list-ii/
# 39ms 14.1MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
        now = start = ListNode(None)
        now.next = head

        # start => 역순 연결리스트 시작전 값, end => 역순 연결리스트의 끝값
        for i in range(left - 1):
            start = start.next
        end = start.next

        # 역순 연결리스트 만들기
        node, prev = start.next, None
        for _ in range(right - left + 1):
            succ, node.next = node.next, prev
            node, prev = succ, node

        # 역순연결리스트의 시작값과 왼쪽 나머지부분 연결
        start.next = prev
        # 역순연결리스트의 끝값과 오른쪽 나머지부분 연결
        end.next = node

        return now.next