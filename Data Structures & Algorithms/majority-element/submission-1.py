class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)/2
        numsHash = {}
        for num in nums:
            if num not in numsHash:
                numsHash[num] = 1
            else:
                numsHash[num] += 1
        
        for key in numsHash:
            if numsHash[key] > m:
                return key
