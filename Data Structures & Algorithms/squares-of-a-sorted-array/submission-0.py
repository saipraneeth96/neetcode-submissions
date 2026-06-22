class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # The largest square always comes from one end of the array
        n = len(nums)
        answer = [0]*n
        i, j, k = 0, n-1, n-1

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                answer[k] = nums[i] ** 2
                i += 1
            else:
                answer[k] = nums[j] ** 2
                j -= 1
            k -= 1

        return answer