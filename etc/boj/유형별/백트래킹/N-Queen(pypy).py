def queen(chess, n, x):
    count = 0
    if n == x:
        return 1
    for y in range(n):
        # (x, y)에 퀸을 놓음
        chess[x] = y
        # for - else 구문
        for k in range(x):
            # 세로로 겹치는 경우 세지않음
            if chess[k] == chess[x]:
                break
            # 대각으로 겹치는 경우 세지않음
            if abs(chess[k] - chess[x]) == abs(x - k):
                break
        # for 문이 모두 실행된 경우 => 체스판에 퀸을 둔경우
        # 다음 수를 두고 계속해서 체스판이 완성되면(n == x) 리턴값(1)을 더함
        else:
            count = count + queen(chess, n, x + 1)
    return count


n = int(input())
chess = [0] * n
print(queen(chess, n, 0))

# pypy와 CPython의 차이
# pypy JIT컴파일을 도입하여 CPython 보다 빠르다
# pypy는 자주쓰이는 코드를 캐싱하는 기능이 있기때문에
# 메모리를 사용하여 실행속도를 개선하였고
# 반복문을 많이 사용하는 코드에서는 pypy가 속도측에서 우세하다.
# 간단한 코드상에서는 Python3가 메모리, 속도 측에서 우세할 수 있는 것이고,
# 복잡한 코드(반복)을 사용하는 경우에서는 PyPy3가 우세하기 때문에 적절히 사용

# 실제로 모든경우를 검사하는 브루트포스나 모든 경우 탐색하는 백트래킹 문제에서
# python은 오답이지만 pypy는 정답인 경우 있었음 (N-queen, 마인크래프트)
# https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4
