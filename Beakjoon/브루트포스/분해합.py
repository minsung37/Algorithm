# 분해합을 입력값으로 받음
n = int(input())

# 생성자 찾기
for i in range(1, n+1):
    # i의 각 자릿수를 더함
    num = sum((map(int, str(i))))
    # 분해합 = 생성자 + 생성자의 각 자리수합
    num_sum = i + num
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    # 생성자가 존재하지 않을때
    if i == n:
        print(0)