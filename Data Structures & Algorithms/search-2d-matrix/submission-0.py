class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix: 
            l = set(i)
            if target in l:
                return True
        return False