class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum, left_sum = 0, 0
        for i in range(1, len(nums)):
            right_sum += nums[i]

        if left_sum == right_sum:
            return 0

        for i in range(0, len(nums)-1):
            left_sum += nums[i]
            right_sum -= nums[i+1]
            
            if left_sum == right_sum:
                return i+1

        return -1