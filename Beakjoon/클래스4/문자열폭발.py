# 단어와 폭발문자열 입력받기
word = input()
bomb = input()
m = len(word)
n = len(bomb)

# 스택에 알파벳하나씩 넣기
stack = []
for i in range(m):
    stack.append(word[i])
    # 스택에 넣은 문자가 폭발 문자열의 마지막과 일치하는경우
    if stack[-1] == bomb[-1]:
        count = 0
        # 스택의 길이가 폭발 문자열의 길이보다 크거나 같은경우
        if len(stack) >= n:
            # 스택과 폭발문자열을 비교
            for j in range(n):
                if stack[- 1 - j] == bomb[- 1 - j]:
                    # 같은문자열이 나오면 count
                    count = count + 1
            # count 횟수가 폭발문자열의 길이와 같은경우
            if count == n:
                # 스택에서 차례로 빼줌
                for k in range(n):
                    stack.pop()

# 문자열이 없는경우
if len(stack) == 0:
    print("FRULA")
else:
    # 스택안에 있는 문자들을 문자열 형태로 만듦
    answer = ''.join(stack)
    print(answer)
