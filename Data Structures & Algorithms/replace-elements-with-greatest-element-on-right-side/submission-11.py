class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr2 = [0]*n
        maxNum = -1
        arr2[n-1] = -1
        for i in range(n-2, -1, -1):
            maxNum = max(maxNum, arr[i+1])
            arr2[i] = maxNum
        return arr2