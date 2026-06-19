class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2, i = len(word1), len(word2), 0
        result = ""

        while i < n1 and i < n2:
            result += word1[i]
            result += word2[i]
            i += 1

        if i == n1:
            result += word2[i:]
        
        if i == n2:
            result += word1[i:]

        return result