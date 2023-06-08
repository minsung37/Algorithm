n = list(input())
front, back = 0, 0

k = len(n) // 2
for i in range(k):
    front = front + int(n[i])
    back = back + int(n[i + k])
if front == back:
    print("LUCKY")
else:
    print("READY")