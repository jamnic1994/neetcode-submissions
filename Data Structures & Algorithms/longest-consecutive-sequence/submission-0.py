class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        current_length, longest = 0, 0
        numbers = set(nums)

        for num in numbers:
            if num - 1 not in numbers:
                current_length = 1
                current_num = num + 1

                while current_num in numbers:
                    current_length += 1
                    current_num += 1
                
                longest = max(longest, current_length)
        
        return longest
