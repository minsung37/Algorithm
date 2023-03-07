from collections import Counter
n = input()
n = n.upper()

cnt = Counter(n).most_common()
if len(n) == 1:
    print(n[0])
else:
    if cnt[0][1] == cnt[1][1]:
        print("?")
    else:
        print(cnt[0][0])