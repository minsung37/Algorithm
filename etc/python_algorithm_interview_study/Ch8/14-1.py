# https://leetcode.com/problems/merge-two-sorted-lists/
# 47ms 13.9MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        current = ListNode()
        # 처음 시작위치 저장
        start = current
        # list1과 list2가 존재할때
        while list1 and list2:
            # list2의 값이 더크면
            if list1.val < list2.val:
                # 다음값으로 list1 선택
                current.next = list1
                list1 = list1.next
            # list1의 값이 더 크면
            else:
                # 다음값으로 list2 선택
                current.next = list2
                list2 = list2.next
            current = current.next
        # 남은거 이어붙이기
        current.next = list1 or list2
        # start 이후로 리턴
        return start.next