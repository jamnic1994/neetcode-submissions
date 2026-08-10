class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resultList = [1] * n

        prefix = 1
        for i in range(n):
            resultList[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            resultList[i] *= suffix
            suffix *= nums[i]

        return resultList