n = int(input())
for t in range(n):
    memory_list = input()
    current, count = 1, 0
    for memory in memory_list:
        if current == int(memory):
            count = count + 1
            current = (current + 1) % 2
    print("#{} {}".format(t + 1, count))