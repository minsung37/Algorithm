import sys
input = sys.stdin.readline


def dac(order, left, right):
    if order == 0:
        return
    partition = (right - left + 1) // 3
    dac(order - 1, left, left + partition - 1)
    for i in range(left + partition, left + 2 * partition):
        answer[i] = " "
    dac(order - 1, left + 2 * partition, right)


while True:
    try:
        n = int(input())
        answer = ['-'] * (3 ** n)
        dac(n, 0, 3 ** n - 1)
        print(''.join(answer))
    except:
        break