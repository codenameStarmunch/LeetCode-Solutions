
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        maximum_array = nums[0]

        for x in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += x
            maximum_array = max(maximum_array, current_sum)

        return maximum_array