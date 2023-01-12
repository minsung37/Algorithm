# 단어개수
n = int(input())

# 단어 체크
checker = 0
for i in range(n):
    word = input()
    b = set(word)
    # 단어의 문자가 모두 다른경우 => 그룹단어
    if len(word) == len(b):
        checker = checker + 1
    # 중복된 문자를 포함 하는 경우
    else:
        result = word[0]
        for j in range(1, len(word)):
            # 연속되지않은 알파벳 추가
            if word[j - 1] != word[j]:
                result = result + word[j]
        # 개수가 다르면 같은 문자가 서로 떨어져있다.
        if len(b) == len(result):
            checker = checker + 1

# 정답 출력
print(checker)