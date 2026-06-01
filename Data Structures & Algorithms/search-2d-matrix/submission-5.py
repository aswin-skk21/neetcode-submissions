class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) * len(matrix) - 1

        while l <= r: 
            mid = (l + r) // 2
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] > target:
                r = mid - 1
            elif matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
                l = mid + 1
            else: 
                return True
        
        return False