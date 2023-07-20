# https://programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범
import collections


def solution(genres, plays):
    answer = []
    genre_sort = collections.defaultdict(int)
    genre_dic = collections.defaultdict(list)

    for index, genre in enumerate(genres):
        genre_dic[genre].append([plays[index], index])
        if genre_sort[genre]:
            genre_sort[genre] = genre_sort[genre] + plays[index]
        else:
            genre_sort[genre] = plays[index]

    # 많이 재생된 장르순 정렬
    genre_sort = sorted(genre_sort, reverse=True, key=lambda x: genre_sort[x])
    for i in genre_sort:
        # 장르내에서 많이 재생된 노래, 같으면 고유번호 낮은 노래를 먼저 수록
        music = sorted(genre_dic[i], reverse=True, key=lambda x: (x[0], -x[1]))
        for j in music[:2]:
            answer.append(j[1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", "aock"], [500, 600, 150, 800, 2500, 15011]))