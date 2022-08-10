# https://leetcode.com/problems/merge-k-sorted-lists/
# 98ms 18.5MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeKLists(lists: list[ListNode]) -> ListNode:
        # 배열에 담기
        result = []
        for i in lists:
            linked_list = i
            while linked_list is not None:
                result.append(linked_list.val)
                linked_list = linked_list.next
        result.sort()
        # 배열 => 연결리스트
        curr = head = ListNode()
        for r in result:
            node = ListNode(r)
            curr.next = node
            curr = curr.next
        return head.next