class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if i == j:
                    result = result
                else:
                    result = result * nums[j]
            output.append(result)
        return output
