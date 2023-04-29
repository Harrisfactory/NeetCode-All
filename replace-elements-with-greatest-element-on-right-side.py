class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) <= 1:
            return [-1]

        for i in range(len(arr)):
            if i + 1 < len(arr):
                arr[i] = max(arr[i + 1:len(arr)])

        
        arr[len(arr) - 1] = -1
        return arr