class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
                if freq[num] >= 2:
                    return True
            else:
                freq[num] = 1

        return False