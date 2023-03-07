sound = list(map(int, input().split()))

aa = [1,2,3,4,5,6,7,8]
bb = [8,7,6,5,4,3,2,1]

if sound == aa:
    print("ascending")
elif sound == bb:
    print("descending")
else:
    print("mixed")