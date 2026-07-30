class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # lrow, rrow = 0, len(matrix[0])
        # lcol, rcol = 0, len(matrix[1])

        # while lrow < rrow:
        #     midrow = lrow + lcol
        #     while lcol < rcol:
        #         midcol


        width = len(matrix[0])
        heigth = len(matrix)
        l, r = 0, width*heigth - 1 # ricorda sempre il -1

        while l <= r:
            mid = (l + r) // 2
            coorX = mid // width
            coorY = mid % width
            if (matrix[coorX][coorY] == target):
                return True
            elif (matrix[coorX][coorY] < target):
                l = mid + 1
            else:
                r = mid - 1

        return False






