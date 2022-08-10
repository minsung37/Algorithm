# https://leetcode.com/problems/add-two-numbers/
# 84ms 13.9MB
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        # 두수의 합
        first, second = '', ''
        while l1:
            first = first + str(l1.val)
            l1 = l1.next
        while l2:
            second = second + str(l2.val)
            l2 = l2.next
        two_sum = str(int(first[::-1]) + int(second[::-1]))

        # 합이 0인 경우
        if two_sum == "0":
            return ListNode(0)

        # 역순연결리스트 만들기
        result = ListNode(two_sum[-1])
        node = result
        for val in two_sum[-2::-1]:
            node.next = ListNode(val)
            node = node.next
        return result
