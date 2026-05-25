class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        h = len(arr)
        for i in range(h-1):
            k = max(arr[i+1:])
            arr[i] = k
        arr[h-1] = -1
        return arr



"""
range(len(arr)-1)


"""