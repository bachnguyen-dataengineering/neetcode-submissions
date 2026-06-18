class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            tempSum = numbers[i] + numbers[j]
            if tempSum > target:
                j -= 1
            elif tempSum < target:
                i += 1
            else:
                break
        return [i+1,j+1]