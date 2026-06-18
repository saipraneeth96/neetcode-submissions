class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dup = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[dup]:
                dup += 1
                nums[dup] = nums[i]

        return dup + 1