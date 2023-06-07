# RGB거리2
# https://www.acmicpc.net/problem/17404
import copy
import sys
input = sys.stdin.readline


def dynamic_programming(dp):
    for i in range(1, n):
        for color in range(3):
            if i == n - 1:
                temp = []
                for next_color in range(3):
                    if next_color != first_color[i - 1][color] and next_color != color:
                        temp.append(dp[i][next_color])
                result.append(dp[i - 1][color] + min(temp))
                continue
            dp[i][color] = dp[i][color] + min(dp[i - 1][(color + 1) % 3], dp[i - 1][(color + 2) % 3])
            if i == 1:
                if dp[i - 1][(color + 1) % 3] > dp[i - 1][(color + 2) % 3]:
                    first_color[i][color] = (color + 2) % 3
                else:
                    first_color[i][color] = (color + 1) % 3
            else:
                if dp[i - 1][(color + 1) % 3] > dp[i - 1][(color + 2) % 3]:
                    first_color[i][color] = first_color[i - 1][(color + 2) % 3]
                else:
                    first_color[i][color] = first_color[i - 1][(color + 1) % 3]


n = int(input())
dp_origin = [list(map(int, input().split())) for _ in range(n)]

dp_reversed = copy.deepcopy(dp_origin)
dp_reversed.reverse()

result, first_color = [], [[0] * 3 for _ in range(n)]

dynamic_programming(dp_origin)
dynamic_programming(dp_reversed)

print(min(result))