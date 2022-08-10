import sys
input = sys.stdin.readline
# 포켓몬, 문제개수 입력받기
n, m = map(int, input().split())
pokemon = []
for _ in range(n):
    pokemon.append(input().rstrip())

# 문제정보 입력받기
target = []
for _ in range(m):
    a = input().rstrip()
    target.append(a)

# 숫자를 int로 변경
for i in range(m):
    try:
        target[i] = int(target[i])
    except:
        continue

# 정답 출력
for i in range(m):
    if type(target[i]) == int:
        print(pokemon[target[i] - 1])
    else:
        print(pokemon.index(target[i]) + 1)