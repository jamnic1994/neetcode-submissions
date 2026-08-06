class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sum = []
        diff = 0

        for i in range(len(nums)):
            diff = target - nums[i]

            for j in range(len(nums)):
                if diff == nums[j] and i != j:
                    sum.append(i)
                    sum.append(j)

                    return sum
