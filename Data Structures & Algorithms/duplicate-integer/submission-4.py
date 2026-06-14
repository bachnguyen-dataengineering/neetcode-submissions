class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = {}
        for num in nums:
            if num not in hashSet:
                hashSet[num] = 1
            else:
                return True
        return False
            