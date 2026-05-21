class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    
    # for index i, if nums[i] = 1 then do:
    # for index j in range(i, len(nums)), if j = 1 then temp_count +=1, if j = 0 then break
    # compare if temp_count >= act_count then replace

        n = len(nums)
        max_count = 0

        for i in range(n):
            temp_count = 0

            if nums[i] == 1:
                for j in range(i,n):
                    if nums[j] == 0: 
                        break
                    else:
                        temp_count += 1
            if temp_count >= max_count:
                max_count = temp_count
        return max_count