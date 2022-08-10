# https://leetcode.com/problems/group-anagrams/
# 그룹 에너그램 - 93ms 17.2MB
class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        anagram = {}
        # 정렬후 딕셔너리에 key-value 형태로 담기 => 같은 구성은 같은 키값으로들어감
        for value in strs:
            key = ''.join(sorted(value))
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(value)
        result = [anagram[key] for key in anagram]
        return result