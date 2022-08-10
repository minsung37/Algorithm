n = list(input())
word, num = [], []
for i in n:
    try:
        num.append(int(i))
    except:
        word.append(i)
word.sort()
print(''.join(word), end="")
print(sum(num))