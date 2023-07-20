def recursion(word):
    global result
    if len(word) == len(a):
        if "".join(word) == a:
            result = 1
        return
    # 문자열의 뒤에 A를 추가한다.
    if word[-1] == "A":
        word.pop()
        recursion(word)
        word.append("A")
    # 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
    if word[0] == "B":
        word = word[1:]
        word.reverse()
        recursion(word)


a, b = input(), list(input())
result = 0
recursion(b)
print(result)