class Solution:
    def firstUniqChar(self, s: str) -> int:
        nrepeat = {}

        for i in range(len(s)):
            if s[i] not in nrepeat:
                nrepeat[s[i]] = 1
            else:
                nrepeat[s[i]] += 1

        for i in range(len(s)):
            if nrepeat[s[i]] == 1:
                return i

        return -1