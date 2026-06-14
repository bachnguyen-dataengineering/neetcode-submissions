class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        maxCountTemp = 0
        for num in nums:
            if num == 1:
                maxCountTemp += 1
                maxCount = max(maxCount, maxCountTemp)
            else:
                maxCountTemp = 0
        return maxCount