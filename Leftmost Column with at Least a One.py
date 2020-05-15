class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        row, col = binaryMatrix.dimensions()
        
        i, j = 0, col-1
        left = col
        while i <= row - 1 and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            elif binaryMatrix.get(i, j) == 1:
                if j < left:
                    left = j
                j -= 1
        if left == col:
            return -1
        return left