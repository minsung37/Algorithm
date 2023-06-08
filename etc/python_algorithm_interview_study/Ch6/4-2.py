# https://leetcode.com/problems/most-common-word/
# 가장흔한 단어 - 48ms 13.9MB(책풀이)
import collections
import re


class Solution:
    @staticmethod
    def mostCommonWord(paragraph: str, banned: list[str]) -> str:
        # 특수문자, 공백제거, 소문자로 만들고 금지단어 아닌거 배열에 담기
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        # 빈도수
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

