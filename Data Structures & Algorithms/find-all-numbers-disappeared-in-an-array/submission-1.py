class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            curr_index = nums[i] - 1
            if nums[i] == nums[curr_index]:
                i = i + 1
            else:
                nums[i], nums[curr_index] = nums[curr_index], nums[i]

        result = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)

        return result