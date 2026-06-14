class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashVar = {}
        for i in range(len(nums)):
            hashVar[target - nums[i]] = i
            # [1,3,4,2] Target 6
            # hashVar {5:0, 3:1, 2:2, 4:3}
        for j in range(len(nums)):
            if nums[j] in hashVar:
                if j > hashVar[nums[j]]:
                    return [hashVar[nums[j]], j]
                elif j < hashVar[nums[j]]:
                    return [j, hashVar[nums[j]]]
                else:
                    continue
            