class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue

            j = i + 1
            k = len(nums)-1

            while j < k:
                threeSum = value + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([value, nums[j], nums[k]])
                    k -= 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
        return res

