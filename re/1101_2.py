# 주식
# https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    array = list(map(int, input().split()))
    cost = 0
    stack = []
    while array:
        k = array.pop()
        if stack:
            if stack[-1] > k:
                cost = cost + stack[-1] - k
            else:
                stack.clear()
                stack.append(k)
        else:
            stack.append(k)
    print(cost)