# 1~ 10000까지 담을변수
natural = set(range(1, 10001))

# 셀프넘버가 아닌것을 담을 변수
generate = set()
for i in natural:
    for j in str(i):
        i = i + int(j)
    generate.add(i)

# 셀프넘버
self = sorted(natural - generate)

# 정답출력
for i in self:
    print(i)
