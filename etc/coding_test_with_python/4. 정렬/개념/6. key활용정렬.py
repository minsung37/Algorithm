array = [('사과', 5), ('바나나', 2), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)