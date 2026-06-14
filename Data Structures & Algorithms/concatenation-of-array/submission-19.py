class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums2 = [0]* (2*n)

        for i in range(n):
            nums2[i] = nums2[n+i] = nums[i]
        return nums2