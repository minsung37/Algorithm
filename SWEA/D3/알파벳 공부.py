# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXAdrmW61ssDFAXq
# 9480. 민정이와 광직이의 알파벳 공부
def is_have_all_alphabet(word):
    for askii in range(ord('a'), ord('z') + 1):
        if chr(askii) not in word:
            return False
    return True


def backtraking(word, index, visit):
    global visited
    # 알파벳이 모두 있는경우
    if is_have_all_alphabet(word):
        visited.add(visit)
    # 범위벗어난 경우
    if index == n:
        return
    new_word = set()
    for i in word:
        new_word.add(i)
    for i in words[index]:
        new_word.add(i)
    backtraking(word, index + 1, visit)
    backtraking(new_word, index + 1, visit + str(index))


T = int(input())
for t in range(T):
    n = int(input())
    words = [input() for _ in range(n)]
    visited = set()
    backtraking(set(), 0, "")
    print(visited)
    print('#{} {}'.format(t + 1, len(visited)))