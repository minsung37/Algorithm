# [3차] 파일명 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution2(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(s) for s in sort]


def solution(files):
    num_list, file_name_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], []

    for file in files:
        number, head, tail = "", "", ""
        for index, alpa in enumerate(file):
            if alpa in num_list:
                head = file[:index]
                number = file[index:]
                for index_, alpa_ in enumerate(number):
                    if alpa_ not in num_list:
                        tail = number[index_:]
                        number = number[:index_]
                        break
                file_name_list.append([head, number, tail])
                break

    file_name_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(file_name) for file_name in file_name_list]


print(solution2(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution2(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]