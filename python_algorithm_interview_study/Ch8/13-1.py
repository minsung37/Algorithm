# https://leetcode.com/problems/palindrome-linked-list/
# 1379ms 47MB (책풀이 - 리스트 변환)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def isPalindrome(head: ListNode) -> bool:
        if not head:
            return True

        # 리스트 변환
        palindrome = []
        while head is not None:
            palindrome.append(head.val)
            head = head.next

        # 팰린드롬 판별
        while len(palindrome) > 1:
            if palindrome.pop(0) != palindrome.pop():
                return False
        return True