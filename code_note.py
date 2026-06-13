ARRAY
-- Sample Code
--- PrefixSum:
class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left > 0 else 0
        return (preRight - preLeft)



-- Leetcode
--- Range Sum Query Immutable
---- Using PrefixSum I:
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)

---- Using PrefixSum II:
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) +1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


--- Valid Word Square
