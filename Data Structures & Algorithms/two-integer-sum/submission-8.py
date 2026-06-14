class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listed = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in listed:
                return [listed[num2], i]
            
            listed[num] = i