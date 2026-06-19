class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numsHash = {}

        for num in nums:
            if num not in numsHash:
                numsHash[num] = 1
            else:
                numsHash[num] += 1
        
        maxVal = -1
        for key in numsHash:
            if numsHash[key] == 1:
                maxVal = max(maxVal, key)
        
        return maxVal

