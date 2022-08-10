import sys
input = sys.stdin.readline

# 트리 만들기
n = int(input())
tree = [[] for _ in range(n)]
array = list(map(int, input().split()))
for i in range(n):
    tree[i] = array[i]

# 삭제할 노드 입력받기
xxx = int(input())


# xxx가 포함된 항목 삭제하기
def delete(xxx):
    # xxx의 자식
    tree[xxx] = -2
    for i in range(n):
        if tree[i] == xxx:
            tree[i] = -2
            delete(i)


delete(xxx)
count = 0
for i in range(n):
    if tree[i] != -2:
        err = 0
        for j in tree:
            if j == i:
                err = 1
                break
        if err == 0:
            count += 1
print(count)
