T = int(input())
for t in range(T):
    n, trees = int(input()), sorted(list(map(int, input().split())))
    target_height = trees.pop()
    for idx, height in enumerate(trees):
        diff = target_height - height
        trees[idx] = diff
    day, water = 0, 1
    while True:
        if trees.count(0) == len(trees):
            break
        watering = False
        # 홀수날
        if water % 2 == 1:
            for idx, tree in enumerate(trees):
                if tree == 0:
                    continue
                # 홀수나무 에 물주기
                if tree % 2 == 1:
                    trees[idx] = trees[idx] - 1
                    watering = True
                    break
            # 홀수 나무 없는 경우
            if not watering:
                zero_count = trees.count(0)
                for idx, tree in enumerate(trees):
                    # 2하나 남은 경우 패스
                    if tree == 2 and zero_count == len(trees) - 1:
                        continue
                    # 2이상 짝수 물줌
                    if tree > 1:
                        trees[idx] = trees[idx] - 1
                        watering = True
                        break
        # 짝수날
        if water % 2 == 0:
            for idx, tree in enumerate(trees):
                if tree == 0:
                    continue
                # 짝수나무에 물주기
                if tree % 2 == 0:
                    trees[idx] = trees[idx] - 2
                    watering = True
                    break
            if not watering:
                for idx, tree in enumerate(trees):
                    # 짝수 나무 없으면 2이상 홀수에 물주기
                    if tree > 2:
                        trees[idx] = trees[idx] - 2
                        watering = True
                        break
        day = day + 1
        water = (water + 1) % 2
        if trees.count(0) == len(trees):
            break
    print("#{} {}".format(t + 1, day))