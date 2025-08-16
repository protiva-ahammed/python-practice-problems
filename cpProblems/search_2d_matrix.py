from typing import List


class Solution9:
    def searchMatrixBrute(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix) ):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False