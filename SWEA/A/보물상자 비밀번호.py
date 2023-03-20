from collections import deque


T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    rock = deque(input())
    repeat = n // 4
    number = set()
    for _ in range(repeat):
        count, temp = 0, ""
        for i in rock:
            temp = temp + i
            count = count + 1
            if count == repeat:
                number.add(int(temp, 16))
                count, temp = 0, ""
        rock.appendleft(rock.pop())
    number = list(number)
    number.sort(reverse=True)
    print("#{} {}".format(t + 1, number[k - 1]))