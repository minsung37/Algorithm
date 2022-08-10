# https://leetcode.com/problems/most-common-word/
# 가장흔한 단어 - 50ms 13.9MB
import collections


class Solution:
    @staticmethod
    def mostCommonWord(paragraph: str, banned: list[str]) -> str:
        # " "과 "," 기준으로 나누기
        temp_paragraph = str(paragraph.split()).split(",")
        word_in_paragraph = []
        for temp_word in temp_paragraph:
            # 소문자로 만들기 => 특수문자제거 => 금지단어,공백 아닌거 배열에 넣기
            word = ''.join(filter(str.isalnum, temp_word.lower()))
            if word not in banned and len(word) > 0:
                word_in_paragraph.append(word)
        # 빈도수
        count = collections.Counter(word_in_paragraph)
        return count.most_common(1)[0][0]