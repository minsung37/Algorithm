from collections import defaultdict


def solution(topping):
    first, second = defaultdict(int), set()
    count = 0
    for i in topping:
        first[i] = first[i] + 1
    for i in topping:
        first[i] = first[i] - 1
        if first[i] == 0:
            del first[i]
        second.add(i)
        if len(second) == len(first):
            count = count + 1
        if len(second) > len(first):
            break
    return count


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))