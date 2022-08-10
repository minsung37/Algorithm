# https://leetcode.com/problems/merge-two-sorted-lists/
# 33ms 13.8MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        # 1. l1이 None이면, l1과 l2를 무조건 바꾸어야 함
        # 2. 이때, l2가 None이면 바꾸면 안됨
        # 3. l1, l2 노드의 값이 작은 쪽이 l1가 됨
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

        # 이렇게 바꾸었을 때, l1이 None이면 l1, l2둘다 None임
        # 둘다 None이라면 재귀를 더이상 하면 안되기에, if로 체크함
        if list1:
            # l1이 존재하면, l1의 next를 찾기 위한 재귀를 실행
            list1.next = Solution.mergeTwoLists(list1.next, list2)
        return list1