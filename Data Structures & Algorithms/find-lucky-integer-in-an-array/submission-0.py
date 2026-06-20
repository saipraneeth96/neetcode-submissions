class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        maxi = -1

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if key == value:
                lucky = key
                maxi = max(lucky, maxi)

        return maxi