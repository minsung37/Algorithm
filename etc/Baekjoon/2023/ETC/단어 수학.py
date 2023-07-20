from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    temp = input().rstrip()
    words.append(temp)

dic = defaultdict(int)
for word in words:
    for index, alphabet in enumerate(word):
        dic[alphabet] = dic[alphabet] + 10 ** (len(word) - 1 - index)
# value 기준 내림차순 정렬
alpha_sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)

result, number = 0, 9
for i in alpha_sort:
    result = result + number * i[1]
    number = number - 1
print(result)



