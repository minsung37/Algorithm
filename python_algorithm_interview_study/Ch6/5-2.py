# https://leetcode.com/problems/group-anagrams/
# 그룹 에너그램 - 132ms 17.3MB(책풀이)
import collections


class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        anagram = collections.defaultdict(list)
        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        return list(anagram.values())
