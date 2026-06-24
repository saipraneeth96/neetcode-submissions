class Solution:
    def firstUniqChar(self, s: str) -> int:
        nrepeat = {}

        for i in range(len(s)):
            if s[i] not in nrepeat:
                nrepeat[s[i]] = 1
            else:
                nrepeat[s[i]] += 1

        for key, value in nrepeat.items():
            if value == 1:
                return s.index(key)

        return -1