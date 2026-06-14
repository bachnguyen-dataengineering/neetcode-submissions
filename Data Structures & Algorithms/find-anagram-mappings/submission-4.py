class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        n = len(nums2)
        outputArray = []
        for i in range(n):
            hashMap[nums2[i]] = i
        for num in nums1:
            if num in hashMap:
                outputArray.append(hashMap[num])
        return outputArray


