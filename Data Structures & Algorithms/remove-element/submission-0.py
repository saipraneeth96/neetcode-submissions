class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j = j+1
                count += 1

        return count