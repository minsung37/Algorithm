import sys
input = sys.stdin.readline

# 포켓몬, 문제개수 입력받기
n, m = map(int, input().split())

# dict에 번호 : 이름 과 이름 : 번호 값을 저장
pokemon = {}
for i in range(1, n + 1):
    a = input().rstrip()
    pokemon[i] = a
    pokemon[a] = i

# 문제정보 입력받고 바로 정답출력
# isdigit() 함수는 문자열이 숫자로 표시되어 있으면 True반환
# But, 음수나 소수점이 있을경우 False 반환
for i in range(m):
    x = input().rstrip()
    if x.isdigit():
        print(pokemon[int(x)])
    else:
        print(pokemon[x])