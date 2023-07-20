from collections import defaultdict
import sys
input = sys.stdin.readline


n = int(input())
numbers = list(map(int, input().split()))
dic = defaultdict(int)
result, stack = [-1] * n, []

for number in numbers:
    dic[number] = dic[number] + 1

# stack에는 오등큰수 못찾은 원소의 인덱스값 넣음
for index, number in enumerate(numbers):
    # 스택에 값이있고 스택 상단의 오등큰수 발견된 경우
    while stack and dic[number] > dic[numbers[stack[-1]]]:
        result[stack.pop()] = number
    stack.append(index)
print(*result)