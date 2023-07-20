# 입력받은거 + 기준으로 나누기
n = list(map(str, input().split('-')))
plus = "+"

first = n[0]
n.remove(n[0])

# 첫항 => 첫번째 마이너스까지는 모두 더해야함
b = []
if plus in first:
    b = list(map(int, first.split("+")))
    res = sum(b)
else:
    res = int(first)

# 두번째항부터 => 부호에 상관없이 더한뒤에 빼주기
a = []
for i in range(len(n)):
    if plus in n[i]:
        x = list(map(int, n[i].split("+")))
        a = a + x
    else:
        a.append(int(n[i]))
res2 = sum(a)
print(res - res2)