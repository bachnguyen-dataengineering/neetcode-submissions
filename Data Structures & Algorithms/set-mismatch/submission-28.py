class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        numsHash = Counter(nums)
        
        for i in range(1, len(nums) + 1):
            if numsHash[i] == 2:
                res[0] = i
            if numsHash[i] == 0:
                res[1] = i
        
        return res