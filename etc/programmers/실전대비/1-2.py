def solution(want, number, discount):
    my_plan, result = {}, 0
    for index, item in enumerate(want):
        my_plan[item] = number[index]
    for i in range(len(discount) - 9):
        discount_ = discount[i: i + 10]
        market = {}
        for j in discount_:
            market[j] = discount_.count(j)
        count = 0
        for k in want:
            try:
                if market[k]:
                    if my_plan[k] == market[k]:
                        count = count + 1
                    else:
                        break
            except:
                break
        if count == len(want):
            result = result + 1
    return result


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana",
                "apple", "banana"]))

print(solution(["apple"], [10],
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
