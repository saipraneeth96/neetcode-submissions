class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1

        while s[i] == ' ':
            i = i-1

        count = 0
        for k in range(i, -1, -1):
            if s[k] == ' ':
                return count
            else:
                count += 1

        return count