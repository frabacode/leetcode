class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]

        for i, letter in enumerate(first):
            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return first[:i]

        return first
