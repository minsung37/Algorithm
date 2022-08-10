# 10은 2와 5의 곱으로만 만들어진다.
# 2와 5가 몇번 나누어지는지를 구한다.
def count(n,k):
    answer = 0
    while n != 0:
        n = n // k
        answer += n
    return answer


n, m = map(int, input().split())
if m == 0:
    print(0)

else:
    # 2와 5의 개수를 구해서 더 작은 개수를 선택한다.
    print(min(count(n, 2) - count(m, 2) - count(n - m, 2), count(n, 5) - count(m, 5) - count(n - m, 5)))