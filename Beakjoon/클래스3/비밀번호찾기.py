import sys
input = sys.stdin.readline

# 가입한 사이트와 찾을 사이트
n, m = map(int, input().split())
# 가입한 사이트를 딕셔너리에 담기
id_pw = dict(input().split() for i in range(n))
# 찾을 사이트를 key값으로 찾는다.
for i in range(m):
    target = input().rstrip()
    print(id_pw.get(target))