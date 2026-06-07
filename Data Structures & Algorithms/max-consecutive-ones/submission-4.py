class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        total_count = 0
        for num in nums:
            if num == 1:
                total_count += 1
            else:
                if num == 0:
                    max_count = max(max_count, total_count)
                    total_count = 0
        
        max_count = max(max_count, total_count)
        return max_count