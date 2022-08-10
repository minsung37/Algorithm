# https://leetcode.com/problems/palindrome-linked-list/
# 1055ms 47MB (책풀이 - 데크를 이용한 최적화)
# Definition for singly-linked list.
from collections import deque


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
        palindrome = deque()
        while head is not None:
            palindrome.append(head.val)
            head = head.next

        # 팰린드롬 판별
        while len(palindrome) > 1:
            if palindrome.popleft() != palindrome.pop():
                return False
        return True